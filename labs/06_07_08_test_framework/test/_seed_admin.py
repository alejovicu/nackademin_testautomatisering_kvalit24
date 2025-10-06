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
            return
    except urllib.error.HTTPError as e:
        if e.code in (400, 409):
            return
        try:
            login_req = urllib.request.Request(
                f"{BACKEND_URL}/login",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(login_req, timeout=8) as r2:
                if 200 <= r2.getcode() < 300:
                    return
        except Exception:
            pass
        raise
