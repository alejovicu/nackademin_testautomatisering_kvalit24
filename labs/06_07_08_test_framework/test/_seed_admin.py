import os, json, urllib.request, urllib.error


def ensure_admin():
    backend = os.getenv("BACKEND_URL", "http://app-backend:8000").rstrip("/")
    data = json.dumps({"username": "admin", "password": "1234"}).encode("utf-8")
    req = urllib.request.Request(
        f"{backend}/signup",
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=5)
    except urllib.error.HTTPError as e:
        if e.code not in (400, 409):
            raise
