import libs.utils
import requests


def signup_user(username: str, password: str):
    url = libs.utils.get_base_url() + "/signup"
    payload = {"username": username, "password": password}

    try:
        response = requests.post(url, json=payload)
        if response.status_code in (200, 201):
            print(f"User '{username}' created successfully")
        elif response.status_code == 400:
            print(f"User {username} already exists")
        else:
            print(
                f"Failed to create user '{username}': {response.status_code} {response.text}"
            )
    except requests.RequestException as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    print("Creating default users")
    admin_creds = libs.utils.get_admin_credentials()
    signup_user(admin_creds["username"], admin_creds["password"])
    testuser_creds = libs.utils.get_test_user_credentials()
    signup_user(testuser_creds["username"], testuser_creds["password"])
