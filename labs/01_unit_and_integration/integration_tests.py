import requests

BASE_URL = "http://127.0.0.1:8000"

def test_addition():
    # Arrange
    possitive_value = 2
    negative_value  = 3
    url_params = {"a": possitive_value, "b": negative_value}
    expected_result = {"result": 5}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result


# Lab tasks

def test_sum_one_positive_one_negative():
    # Arrange
    url_params = {"a": 7, "b": -3}
    expected_result = {"result": 4}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result
