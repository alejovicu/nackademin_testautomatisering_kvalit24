import os, sys, requests


def main():
    backend = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")
    r = requests.post(
        f"{backend}/signup", json={"username": "admin", "password": "1234"}, timeout=5
    )
    print(f"[seed] admin -> {r.status_code}")
    return 0 if r.status_code in (200, 201, 409) else 2


if __name__ == "__main__":
    raise SystemExit(main())
