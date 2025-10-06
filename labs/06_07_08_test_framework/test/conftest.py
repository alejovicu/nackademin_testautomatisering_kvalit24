import os, time, json, urllib.request, urllib.error
import pytest

BACKEND_URL = os.getenv("BACKEND_URL", "http://app-backend:8000").rstrip("/")


def _get(url, timeout=2):
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.getcode(), r.read().decode()


def _post(url, payload: dict, timeout=5):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.getcode(), r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


@pytest.fixture(scope="session", autouse=True)
def wait_backend_and_seed_admin():
    deadline = time.time() + 60
    last_err = None
    while time.time() < deadline:
        try:
            code, _ = _get(f"{BACKEND_URL}/health", timeout=2)
            if 200 <= code < 300:
                break
        except Exception as e:
            last_err = e
        time.sleep(1)
    else:
        pytest.fail(
            f"Backend is not ready at {BACKEND_URL}/health (last error: {last_err})"
        )

    code, _ = _post(
        f"{BACKEND_URL}/signup", {"username": "admin", "password": "1234"}, timeout=8
    )
    if code not in (200, 201, 409):
        time.sleep(1)
        code, _ = _post(
            f"{BACKEND_URL}/signup",
            {"username": "admin", "password": "1234"},
            timeout=8,
        )
        if code not in (200, 201, 409):
            pytest.fail(f"/signup returned unexpected status: {code}")
