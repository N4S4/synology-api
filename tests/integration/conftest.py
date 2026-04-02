"""
Shared fixtures and configuration for integration tests.

These tests connect to a real Synology NAS. By default, only read-only
(safe) tests run. Destructive tests are skipped unless you explicitly
opt in via the SYNOLOGY_ALLOW_DESTRUCTIVE=1 environment variable.

Setup
-----
1. Copy tests/resources/config-test-sample.json to
   tests/resources/config-test.json
2. Fill in your NAS connection details.
3. Run safe tests:   python3 -m pytest tests/integration/ -m safe -v
4. Run ALL tests:    SYNOLOGY_ALLOW_DESTRUCTIVE=1 python3 -m pytest tests/integration/ -v
"""
import json
import os
import pathlib

import pytest


def _load_config():
    """Load NAS connection config from config-test.json."""
    config_path = os.path.realpath(
        os.path.join(
            pathlib.Path(__file__).parent.parent.resolve(),
            'resources', 'config-test.json'
        )
    )
    if not os.path.exists(config_path):
        pytest.skip(
            "Integration config not found. Copy config-test-sample.json "
            "to config-test.json and fill in your NAS details."
        )
    with open(config_path, 'r') as f:
        return json.load(f)


@pytest.fixture(scope="session")
def nas_config():
    """Provide NAS connection configuration dict."""
    return _load_config()


@pytest.fixture(scope="session")
def nas_connection_kwargs(nas_config):
    """Provide keyword arguments for BaseApi-derived constructors."""
    return dict(
        ip_address=nas_config["synology_ip"],
        port=nas_config["synology_port"],
        username=nas_config["synology_user"],
        password=nas_config["synology_password"],
        secure=bool(nas_config.get("synology_secure", False)),
        cert_verify=False,
        dsm_version=int(nas_config.get("dsm_version", 7)),
        debug=True,
        otp_code=nas_config.get("otp_code"),
    )


# ---------------------------------------------------------------------------
# Custom markers
# ---------------------------------------------------------------------------

def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "safe: read-only test, safe for production NAS")
    config.addinivalue_line(
        "markers", "destructive: write/delete test, may modify NAS state")


def pytest_collection_modifyitems(config, items):
    """Auto-skip destructive tests unless SYNOLOGY_ALLOW_DESTRUCTIVE=1."""
    allow_destructive = os.environ.get(
        "SYNOLOGY_ALLOW_DESTRUCTIVE", "0") == "1"
    if allow_destructive:
        return

    skip_destructive = pytest.mark.skip(
        reason="Destructive test skipped (set SYNOLOGY_ALLOW_DESTRUCTIVE=1 to run)"
    )
    for item in items:
        if "destructive" in item.keywords:
            item.add_marker(skip_destructive)
