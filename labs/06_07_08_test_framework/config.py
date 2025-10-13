import os

BACKEND_URL  = os.getenv("BACKEND_URL")  or os.getenv("APP_BACK_URL")  or "http://localhost:8000"
FRONTEND_URL = os.getenv("FRONTEND_URL") or os.getenv("APP_FRONT_URL") or "http://localhost:5173"