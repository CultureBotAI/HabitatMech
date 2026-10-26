/* Run a page's shipped inline script against a small fake DOM, without a browser.
 *
 * Usage: node site_script_harness.cjs <script.js> <scenario>
 * The script is the inline <script> of a rendered page, extracted by the
 * pytest that calls this. Each scenario builds only the elements that script
 * reads, drives it the way a reader would -- typing, clicking, a slow or failed
 * fetch -- and asserts what the reader would see. Prints "passed: <scenario>".
 */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const [scriptPath, scenario] = process.argv.slice(2);
const source = fs.readFileSync(scriptPath, 'utf8');

function classList() {
  const names = new Set();
  return {
    add: (name) => names.add(name),
    remove: (name) => names.delete(name),
    contains: (name) => names.has(name),
    toggle: (name, force) => {
      const on = force === undefined ? !names.has(name) : Boolean(force);
      if (on) names.add(name); else names.delete(name);
      return on;
    },
  };
}

function element(props = {}) {
  const el = {
    hidden: false, value: '', textContent: '', innerHTML: '', attributes: {}, listeners: {},
    classList: classList(), children: [],
    addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); },
    fire(type, event = {}) { (this.listeners[type] || []).forEach((fn) => fn(event)); },
    getAttribute(name) { return name in this.attributes ? this.attributes[name] : null; },
    setAttribute(name, value) { this.attributes[name] = String(value); },
    appendChild(child) { this.children.push(child); return child; },
    focus() {},
  };
  return Object.assign(el, props);
}

// A <select>: a value no option carries selects nothing, as in a browser.
function select(values) {
  const el = element();
  el.options = values.map((value) => ({ value }));
  let index = 0;
  Object.defineProperty(el, 'value', {
    get() { return index >= 0 ? el.options[index].value : ''; },
    set(value) { index = el.options.findIndex((o) => o.value === String(value)); },
  });
  Object.defineProperty(el, 'selectedIndex', { get: () => index });
  return el;
}

// fetch() whose responses the scenario releases, one URL at a time.
function network() {
  const pending = [];
  const calls = [];
  return {
    calls,
    fetch(url) {
      calls.push(url);
      return new Promise((resolve, reject) => pending.push({ url, resolve, reject }));
    },
    respond(match, body) {
      const index = pending.findIndex((p) => p.url.includes(match));
      assert.ok(index >= 0, `no pending request for ${match}`);
      const [request] = pending.splice(index, 1);
      if (body === undefined) request.reject(new TypeError('Failed to fetch'));
      else if (body.status) request.resolve({ ok: false, status: body.status, json: async () => ({}) });
      else request.resolve({ ok: true, status: 200, json: async () => body });
    },
    get pending() { return pending.map((p) => p.url); },
  };
}

const settle = async () => { for (let i = 0; i < 10; i++) await new Promise((r) => setImmediate(r)); };

function run(context) {
  const base = {
    URL, URLSearchParams, Math, JSON, Number, String, Array, Promise, Object,
    setTimeout, clearTimeout,
    requestAnimationFrame: (fn) => { setImmediate(fn); return 1; },
    Event: class Event { constructor(type) { this.type = type; } },
  };
  vm.runInNewContext(source, Object.assign(base, context));
}

function location(path, search = '') {
  const replaced = [];
  return {
    window: {
      location: { href: `https://site.test/pages/${path}${search}`, search },
      history: { replaceState: (state, title, url) => replaced.push(url) },
    },
    replaced,
  };
}

const rowsIn = (html) => (html.match(/<tr>/g) || []).length;

// ---------------------------------------------------------------- Browse --
function browsePage({ search = '', slugs = ['aquatic', 'host-associated'] } = {}) {
  const net = network();
  const ids = {
    'browse-q': element(),
    'browse-grounding': select(['', 'EXACT', 'UNGROUNDED']),
    'browse-sort': select(['assertions-desc', 'assertions-asc', 'name-asc', 'name-desc', 'grounding-asc']),
    'browse-reset': element(), 'browse-retry': element(),
    'browse-failed': element({ hidden: true }), 'browse-failed-text': element(),
    'browse-more': element({ hidden: true }), 'browse-count': element(),
    'global-hits-wrap': element({ hidden: true }),
  };
  const catRows = slugs.map((slug) => element({
    attributes: { 'data-slug': slug, 'data-label': slug.toUpperCase(), 'data-count': '1' },
    textContent: slug.toUpperCase(),
  }));
  const catBody = element();
  const hitsBody = element();
  const { window, replaced } = location('browse.html', search);
  run({
    window, fetch: net.fetch,
    document: {
      getElementById: (id) => ids[id] || null,
      querySelector: (sel) => ({ '#cat-tbl tbody': catBody, '#global-hits tbody': hitsBody }[sel] || null),
      querySelectorAll: (sel) => (sel === '#cat-tbl tbody tr' ? catRows : []),
    },
  });
  const type = (text) => { ids['browse-q'].value = text; ids['browse-q'].fire('input'); };
  return { ids, net, hitsBody, catRows, type, replaced };
}

const row = (label, slug, grounding = 'EXACT', assertions = 1) => [label, slug, 'Path > ' + label, grounding, assertions, 'GOLD'];

const scenarios = {
  async browse_answers_the_query_typed_while_the_indexes_load() {
    const page = browsePage();
    page.type('g');
    assert.equal(page.ids['browse-count'].textContent, 'Loading category indexes…');
    assert.deepEqual(page.net.calls, ['category/aquatic.json', 'category/host-associated.json']);
    page.type('gu');
    page.type('gut');
    assert.equal(page.net.calls.length, 2, 'later keystrokes must not start another load');
    page.net.respond('aquatic', [row('gutter water', 'gutter-water-x'), row('glacier', 'glacier-x')]);
    page.net.respond('host-associated', [row('gut', 'gut-y'), row('gill', 'gill-y')]);
    await settle();
    assert.equal(page.ids['browse-count'].textContent, 'Showing 2 of 2 matching habitats',
      'the answer must be for "gut", the query in the box, not for "g"');
    assert.equal(rowsIn(page.hitsBody.innerHTML), 2);
    assert.ok(page.hitsBody.innerHTML.includes('habitats/gut-y.html'));
    assert.ok(!page.hitsBody.innerHTML.includes('glacier'));
  },

  async browse_names_a_failed_index_and_recovers_on_retry() {
    const page = browsePage();
    page.type('gut');
    page.net.respond('aquatic', [row('gutter water', 'gutter-water-x')]);
    page.net.respond('host-associated', { status: 404 });
    await settle();
    const count = page.ids['browse-count'].textContent;
    assert.equal(count, 'Search unavailable: 1 of 2 category indexes did not load.');
    assert.equal(page.ids['browse-failed'].hidden, false, 'the failure is shown beside the results');
    assert.ok(page.ids['browse-failed-text'].textContent.endsWith('Retry, or open a category below.'));
    assert.equal(page.ids['global-hits-wrap'].hidden, true, 'no partial result is shown');
    assert.ok(page.catRows.every((tr) => !tr.classList.contains('is-hidden')),
      'every category stays visible as the route that still works');
    page.type('gutt');
    assert.equal(page.net.calls.length, 2, 'typing does not retry by itself');
    assert.ok(page.ids['browse-count'].textContent.startsWith('Search unavailable'));
    page.ids['browse-retry'].fire('click');
    assert.equal(page.net.calls.length, 4, 'retry loads every index again, keeping none');
    page.net.respond('aquatic', [row('gutter water', 'gutter-water-x')]);
    page.net.respond('host-associated', [row('gut', 'gut-y')]);
    await settle();
    assert.equal(page.ids['browse-count'].textContent, 'Showing 1 of 1 matching habitats');
    assert.equal(page.ids['browse-failed'].hidden, true);
    assert.equal(page.ids['global-hits-wrap'].hidden, false);
  },

  async browse_network_error_is_reported_not_counted_as_empty() {
    const page = browsePage();
    page.type('sediment');
    page.net.respond('aquatic');
    page.net.respond('host-associated');
    await settle();
    const count = page.ids['browse-count'].textContent;
    assert.ok(count.startsWith('Search unavailable: 2 of 2'), count);
    assert.ok(!/Showing 0 of 0/.test(count));
  },

  async browse_reaches_every_match_beyond_the_first_page() {
    const page = browsePage({ slugs: ['aquatic'] });
    page.type('marine');
    page.net.respond('aquatic', Array.from({ length: 450 }, (_, n) => row(`marine ${n}`, `marine-${n}`)));
    await settle();
    assert.equal(rowsIn(page.hitsBody.innerHTML), 200);
    assert.equal(page.ids['browse-count'].textContent, 'Showing 200 of 450 matching habitats');
    assert.equal(page.ids['browse-more'].hidden, false);
    page.ids['browse-more'].fire('click');
    assert.equal(rowsIn(page.hitsBody.innerHTML), 400);
    page.ids['browse-more'].fire('click');
    assert.equal(rowsIn(page.hitsBody.innerHTML), 450);
    assert.equal(page.ids['browse-count'].textContent, 'Showing 450 of 450 matching habitats');
    assert.equal(page.ids['browse-more'].hidden, true, 'nothing left to show');
    page.type('marine 1');
    assert.equal(rowsIn(page.hitsBody.innerHTML), 111, 'a new query starts again from one page');
  },

  async browse_restores_only_values_the_page_offers() {
    // A select given a value it lacks selects nothing (selectedIndex -1); the
    // page must leave such a control on its default option instead.
    const page = browsePage({ search: '?q=gut&grounding=RETIRED_STATUS&sort=retired-order' });
    assert.equal(page.ids['browse-grounding'].selectedIndex, 0, 'an unknown grounding keeps "All"');
    assert.equal(page.ids['browse-sort'].value, 'assertions-desc', 'an unknown sort keeps the default');
    assert.equal(page.ids['browse-q'].value, 'gut');
    const known = browsePage({ search: '?q=gut&grounding=EXACT&sort=name-desc' });
    assert.equal(known.ids['browse-grounding'].value, 'EXACT', 'a value the page offers is restored');
    assert.equal(known.ids['browse-sort'].value, 'name-desc');
    page.net.respond('aquatic', [row('gut', 'gut-y', 'UNGROUNDED')]);
    page.net.respond('host-associated', []);
    await settle();
    assert.equal(page.ids['browse-count'].textContent, 'Showing 1 of 1 matching habitats');
  },

  // -------------------------------------------------------------- Category --
  async category_failed_index_offers_retry() {
    const net = network();
    const box = element({ attributes: { 'data-index': 'aquatic.json', 'data-total': '468' } });
    const ids = {
      q: box, count: element(), 'grounding-filter': select(['', 'EXACT']),
      'source-filter': select(['', 'GOLD']),
      'sort-select': select(['assertions-desc', 'label-asc']),
      'show-more': element({ hidden: true }), 'clear-filter': element({ hidden: true }),
      'filter-retry': element({ hidden: true }), 'unfiltered-count': element(),
    };
    const body = element({ innerHTML: '<tr>static page</tr>', querySelectorAll: () => [] });
    const { window } = location('category/aquatic.html');
    run({
      window, fetch: net.fetch,
      document: {
        getElementById: (id) => ids[id] || null,
        querySelector: (sel) => ({ '#tbl tbody': body, '.pager': element() }[sel] || null),
        querySelectorAll: () => [],
      },
    });
    box.value = 'sediment';
    box.fire('input');
    box.value = 'sedimen';
    box.fire('input');
    assert.equal(net.calls.length, 1, 'one request at a time');
    net.respond('aquatic.json');
    await settle();
    assert.ok(ids.count.textContent.startsWith('Filter unavailable: the index of all 468 records did not load'),
      ids.count.textContent);
    assert.equal(ids['filter-retry'].hidden, false);
    assert.equal(body.innerHTML, '<tr>static page</tr>', 'the page keeps its own rows');
    ids['filter-retry'].fire('click');
    assert.equal(net.calls.length, 2);
    assert.equal(ids['filter-retry'].hidden, true);
    net.respond('aquatic.json', [row('marine sediment', 'marine-sediment-x'), row('sea water', 'sea-water-x')]);
    await settle();
    assert.equal(ids.count.textContent, 'Showing 1–1 of 1 matching records (468 in category)',
      'the answer is for the query in the box when the index lands');
  },

  // -------------------------------------------------------------- Text map --
  async map_table_lists_the_plotted_records_and_follows_the_search() {
    const MARKUP = '<img src=x onerror=alert(1)>';
    const points = [
      { identifier: 'ENVO:03000033', label: 'marine sediment', category: 'AQUATIC', page: 'habitats/marine-sediment-envo-03000033.html', x: 1.234, y: -2 },
      { identifier: 'habitatmech:GOLD.0000000001', label: MARKUP, category: 'OTHER', page: 'habitats/x-habitatmech-gold-0000000001.html', x: 0, y: 0 },
      { identifier: 'BTO:0000001', label: 'odd point', category: 'OTHER', page: 'javascript:alert(1)', x: 0, y: 0 },
    ];
    const page = mapPage({ points });
    page.frame.fire('load');
    assert.equal(page.ids['map-status'].textContent, '3 matching records.');
    assert.equal(page.body.innerHTML, '', 'rows are built only when the table opens');
    page.open();
    assert.equal(rowsIn(page.body.innerHTML), 3);
    assert.ok(page.body.innerHTML.includes('<a href="../habitats/marine-sediment-envo-03000033.html">marine sediment</a>'));
    assert.ok(page.body.innerHTML.includes('&lt;img src=x onerror=alert(1)&gt;'), 'a label is text, never markup');
    assert.ok(!page.body.innerHTML.includes('javascript:'), 'a page that is not a record page is not linked');
    assert.ok(page.body.innerHTML.includes('<td class="num">1.23</td>'));
    assert.equal(page.ids['map-table-count'].textContent, 'Showing 3 of 3 plotted records.');
    assert.deepEqual(page.net.calls, [], 'the points come from the map page itself');
    page.search('SEDIMENT');
    assert.equal(rowsIn(page.body.innerHTML), 1, 'the table follows the search');
    assert.equal(page.ids['map-table-count'].textContent,
      'Showing 1 of 3 plotted records, filtered by the search above.');
    assert.equal(page.inner.search.value, 'SEDIMENT', 'the map gets the same query');
  },

  async map_failure_is_reported_and_the_table_still_loads() {
    const page = mapPage({ failed: true });
    page.frame.fire('load');
    assert.ok(page.ids['map-status'].textContent.startsWith('The map did not load'),
      page.ids['map-status'].textContent);
    assert.equal(page.ids['map-retry'].hidden, false);
    page.ids['map-retry'].fire('click');
    assert.equal(page.frame.src, '../text-map-source/index.html', 'retry reloads the map');
    assert.equal(page.ids['map-retry'].hidden, true);
    page.open();
    assert.deepEqual(page.net.calls, ['../text-map-source/points.json']);
    page.net.respond('points.json');
    await settle();
    assert.ok(page.ids['map-table-count'].textContent.startsWith('The map data did not load'));
    assert.equal(page.ids['map-table-retry'].hidden, false);
    page.ids['map-table-retry'].fire('click');
    page.net.respond('points.json', [
      { identifier: 'ENVO:1', label: 'soil', category: 'TERRESTRIAL', page: 'habitats/soil-envo-1.html', x: 0, y: 0 }]);
    await settle();
    assert.equal(rowsIn(page.body.innerHTML), 1);
    assert.equal(page.ids['map-table-retry'].hidden, true);
  },
};

function mapPage({ points = [], failed = false } = {}) {
  const net = network();
  const ids = {
    'text-map-view': null, 'map-q': element(), 'map-reset': element(), 'map-status': element(),
    'map-retry': element({ hidden: true }), 'map-table': element({ open: false }),
    'map-table-body': element(), 'map-table-count': element(), 'map-table-retry': element({ hidden: true }),
  };
  const inner = {
    search: element({ dispatchEvent() {} }),
    count: element(),
    points: element({ textContent: JSON.stringify(points) }),
  };
  inner.search.dispatchEvent = () => {
    const q = inner.search.value.toLowerCase();
    const n = points.filter((p) => (p.label + ' ' + p.identifier).toLowerCase().includes(q)).length;
    inner.count.textContent = `${n} matching records.`;
  };
  inner.count.textContent = `${points.length} matching records.`;
  const doc = element({
    readyState: 'complete',
    getElementById: (id) => ({ search: inner.search, 'match-count': inner.count, points: inner.points }[id] || null),
  });
  const frame = element({ attributes: { src: '../text-map-source/index.html' }, src: '../text-map-source/index.html' });
  Object.defineProperty(frame, 'contentDocument', { get: () => (failed ? null : doc) });
  ids['text-map-view'] = frame;
  const { window } = location('text-map/');
  run({
    window, fetch: net.fetch,
    document: {
      getElementById: (id) => ids[id] || null,
      querySelectorAll: () => [],
    },
  });
  const open = () => { ids['map-table'].open = true; ids['map-table'].fire('toggle'); };
  const search = (text) => { ids['map-q'].value = text; ids['map-q'].fire('input'); };
  return { ids, net, frame, inner, body: ids['map-table-body'], open, search };
}

(async () => {
  assert.ok(scenarios[scenario], `unknown scenario ${scenario}`);
  await scenarios[scenario]();
  console.log(`passed: ${scenario}`);
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
