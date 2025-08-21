import requests

BASE_URL = "http://127.0.0.1:8000"

def test_addition():
    # Arrange
    positive_value_1 = 2
    positive_value_2  = 3
    url_params = {"a": positive_value_1, "b": positive_value_2}
    expected_result = {"result": 5}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result
    assert response.status_code == 200


# Lab tasks

## Complete the following tests

def test_sum_one_positive_one_negative():

    # Arrange
    positive_value = 2
    negative_value  = -3
    url_params = {"a": positive_value, "b": negative_value}
    expected_result = {"result": -1}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result  
    assert response.status_code == 200



