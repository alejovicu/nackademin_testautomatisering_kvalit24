import requests

BASE_URL = "http://127.0.0.1:8000"


def test_addition():
    # Arrange
    possitive_value_1 = 2
    possitive_value_2 = 3
    url_params = {"a": possitive_value_1, "b": possitive_value_2}
    expected_result = {"result": 5}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    # Arrange
    possitive_value = 5
    negative_value = -3
    url_params = {"a": possitive_value, "b": negative_value}
    expected_result = {"result": 2}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result
