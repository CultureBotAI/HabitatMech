/* Shared theme toggle: cycles Auto (system) -> Light -> Dark -> Auto.
 * Persists explicit choice in localStorage["mech-theme"] ("light" | "dark");
 * absent key means follow OS prefers-color-scheme. */
(function () {
  var KEY = "mech-theme";
  var root = document.documentElement;

  function saved() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }
  function save(v) {
    try {
      if (v) localStorage.setItem(KEY, v);
      else localStorage.removeItem(KEY);
    } catch (e) {}
  }
  function apply(mode) {
    if (mode === "light" || mode === "dark") {
      root.setAttribute("data-theme", mode);
    } else {
      root.removeAttribute("data-theme");
    }
  }

  apply(saved());

  function label(mode) {
    if (mode === "light") return "\u2600\uFE0E Light";
    if (mode === "dark") return "\u263E Dark";
    return "\u25D0 Auto";
  }
  function next(mode) {
    if (mode === "light") return "dark";
    if (mode === "dark") return null;
    return "light";
  }

  function mount() {
    var nav = document.querySelector("header.site nav, header nav, nav.top");
    if (!nav || nav.querySelector(".theme-toggle")) return;
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "theme-toggle";
    function sync() {
      var cur = saved();
      btn.textContent = label(cur);
      btn.setAttribute("aria-label", "Color theme: " + (cur || "auto") + " (click to cycle)");
      btn.title = "Color theme: " + (cur || "auto") + " — click to switch";
    }
    sync();
    btn.addEventListener("click", function () {
      var n = next(saved());
      save(n);
      apply(n);
      sync();
    });
    nav.appendChild(btn);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
