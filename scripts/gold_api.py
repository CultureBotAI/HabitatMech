#!/usr/bin/env python3
"""Talk to the GOLD API, exchanging the offline token for an access token itself.

GOLD's ENVO triads are the one authoritative grounding source for the 1,949
GOLD-attested records that carry a minted identifier and no ontology term. Every
lexical route this repo has is exhausted against them (#108); a triad is what the
submitter said the sample's environment was, which is a different kind of
evidence entirely.

**Nobody should ever handle the access token.** It lives ~12 hours, so carrying
it by hand means re-pasting it twice a day, and a credential that gets pasted
gets pasted somewhere it shouldn't be. `OFFLINE_TOKEN` is the only secret, it is
read from the environment, and the exchange happens here.

Auth, as far as it can be determined — GOLD publishes none of this. The OpenAPI
spec has `securitySchemes: []`, the swagger-ui page carries no auth notes, and
the help page does not link the API at all:

    GET /exchange?offlineToken=<offline>   ->  access token
    GET /api/v1/...   with  Authorization: Bearer <access>

An offline token is a refresh token, so passing it directly to /api/v1 returns
401 — correctly, and confusingly if you have not seen `typ: Offline` on it.

The offline session can be revoked while the token stays cryptographically
valid, which presents as HTTP 500 wrapping `invalid_grant / Session not active`.
Logging out of the JGI web session appears to do exactly that, so the token must
be minted and then left alone. That is diagnosed explicitly below, because the
raw error says nothing about what to do.

Usage:
    python3 scripts/gold_api.py --check
    python3 scripts/gold_api.py --biosample Gb0011897
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://gold-ws.jgi.doe.gov"
EXCHANGE = f"{BASE}/exchange"
API = f"{BASE}/api/v1"
TIMEOUT = 60


class GoldAuthError(SystemExit):
    """Auth failed in a way worth explaining rather than re-raising."""


def _get(url: str, headers: dict[str, str] | None = None) -> tuple[int, str]:
    request = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8", "replace")


def access_token(offline: str | None = None) -> str:
    """Exchange the offline token for an access token.

    Never returns the offline token, never logs either, and turns GOLD's
    unhelpful 500 into the one sentence that says what to do about it.
    """
    offline = offline or os.environ.get("OFFLINE_TOKEN")
    if not offline:
        raise GoldAuthError(
            "OFFLINE_TOKEN is not set. It lives in ~/.bashrc and must be exported — "
            "without `export` a child process such as this one cannot see it."
        )

    status, body = _get(f"{EXCHANGE}?{urllib.parse.urlencode({'offlineToken': offline})}")
    if status == 200:
        token = body.strip().strip('"')
        # GOLD returns the bare token, but tolerate a JSON envelope.
        if token.startswith("{"):
            token = (json.loads(token).get("access_token") or "").strip()
        if not token:
            raise GoldAuthError("exchange returned 200 with no token in the body")
        return token

    if "Session not active" in body:
        raise GoldAuthError(
            "GOLD rejected the offline token: its Keycloak session is no longer active.\n"
            "The token is still cryptographically valid, which is why its claims look "
            "fine — the server-side session behind it is gone.\n"
            "Logging out of the JGI web session revokes the offline session. Re-mint at "
            f"{BASE}/login?scope=offline_access and then LEAVE THE SESSION ALONE."
        )
    raise GoldAuthError(f"exchange failed: HTTP {status}: {body[:300]}")


def biosamples(token: str, **params: str) -> list[dict]:
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v})
    status, body = _get(f"{API}/biosamples?{query}", {"Authorization": f"Bearer {token}"})
    if status != 200:
        raise SystemExit(f"biosamples: HTTP {status}: {body[:300]}")
    data = json.loads(body)
    return data if isinstance(data, list) else [data]


def triad(sample: dict) -> dict[str, str | None]:
    """The ENVO triad, flattened. Each slot is `{id, label}` or absent."""
    out: dict[str, str | None] = {}
    for field, short in (("envoBroadScale", "broad"), ("envoLocalScale", "local"),
                         ("envoMedium", "medium")):
        term = sample.get(field) or {}
        out[short] = term.get("id")
        out[f"{short}_label"] = term.get("label")
    return out


def gold_path(sample: dict) -> str:
    """The ecosystem path, in the same `A > B > C` form as data/raw/."""
    parts = [sample.get(k) for k in ("ecosystem", "ecosystemCategory", "ecosystemType",
                                     "ecosystemSubtype", "specificEcosystem")]
    return " > ".join(p for p in parts if p and p != "Unclassified")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="exchange the token and report whether auth works. Prints no "
                             "credential.")
    parser.add_argument("--biosample", help="a GOLD biosample id, e.g. Gb0011897")
    parser.add_argument("--study", help="a GOLD study id, e.g. Gs0114298")
    args = parser.parse_args(argv or sys.argv[1:])

    token = access_token()
    if args.check and not (args.biosample or args.study):
        print("auth OK: offline token exchanged for an access token")
        samples = biosamples(token, biosampleGoldId="Gb0011897")
        print(f"api  OK: /api/v1/biosamples returned {len(samples)} record(s)")
        return 0

    samples = biosamples(token, biosampleGoldId=args.biosample or "",
                         studyGoldId=args.study or "")
    print(f"{len(samples)} biosample(s)")
    for sample in samples[:20]:
        t = triad(sample)
        print(f"\n  {sample.get('biosampleGoldId')}  {(sample.get('biosampleName') or '')[:60]}")
        print(f"    path:   {gold_path(sample) or '(none)'}")
        print(f"    broad:  {t['broad'] or '-':16s} {t['broad_label'] or ''}")
        print(f"    local:  {t['local'] or '-':16s} {t['local_label'] or ''}")
        print(f"    medium: {t['medium'] or '-':16s} {t['medium_label'] or ''}")
        for field in ("habitat", "sampleCollectionSite", "sampleBodySite", "hostName"):
            if sample.get(field):
                print(f"    {field}: {str(sample[field])[:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
