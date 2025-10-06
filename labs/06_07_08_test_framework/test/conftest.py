import os, json, time, urllib.request, urllib.error
import pytest

BACKEND_URL = os.getenv("BACKEND_URL", "http://app-backend:8000").rstrip("/")


@pytest.fixture(scope="session", autouse=True)
def ensure_admin():
    # подождать, пока бэк проснётся (до 30 сек)
    for _ in range(30):
        try:
            urllib.request.urlopen(f"{BACKEND_URL}/health", timeout=2).read()
            break
        except Exception:
            time.sleep(1)

    payload = json.dumps({"username": "admin", "password": "1234"}).encode("utf-8")
    req = urllib.request.Request(
        f"{BACKEND_URL}/signup",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    status = None
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            status = r.getcode()
    except urllib.error.HTTPError as e:
        status = e.code

    assert status in (200, 201, 409), f"/signup returned {status}"
