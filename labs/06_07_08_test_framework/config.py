import os
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def setup_admin():

    username  = "nahom_admin"
    password = "1234"

    data= { "username":username, "password": password} 
    requests.post(f"{BACKEND_URL}/signup", json=data)


def setup_user():

    username = "nahom50"
    password = "nahom50"

    data={"username":username, "password": password} 
    requests.post(f"{BACKEND_URL}/signup",json=data)



setup_admin()
setup_user()