import os, time, json, urllib.request, urllib.error

BACKEND_URL = os.getenv("BACKEND_URL", "http://app-backend:8000").rstrip("/")


def ensure_admin():
    deadline = time.time() + 30
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"{BACKEND_URL}/health", timeout=2).read()
            break
        except Exception:
            time.sleep(1)

    data = json.dumps({"username": "admin", "password": "1234"}).encode("utf-8")
    req = urllib.request.Request(
        f"{BACKEND_URL}/signup",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            pass
    except urllib.error.HTTPError as e:
        if e.code != 409:
            raise
