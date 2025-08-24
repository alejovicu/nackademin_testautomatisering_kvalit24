import requests
import main

BASE_URL = "http://127.0.0.1:8000"


def test_addition():
    # Arrange
    possitive_value = 2
    other_value = 3
    url_params = {"a": possitive_value, "b": other_value}
    expected_result = {"result": 5}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.json() == expected_result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    positive_value = 10
    negative_value = -15
    url_params = {"a": positive_value, "b": negative_value}
    expected_result = {"result": -5}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_sum_one_positive_one_string_value():
    positive_value = 10
    string_value = "Hello, World"
    url_params = {"a": positive_value, "b": string_value}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code in (400, 422)


def test_divide_two_positive_values():
    positive_value1 = 10
    positive_value2 = 2
    url_params = {"a": positive_value1, "b": positive_value2}
    expected_result = {"result": 5.0}

    # Act
    response = requests.get(f"{BASE_URL}/division", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_divide_by_zero():
    # Arrange
    url_params = {"a": 10, "b": 0}

    # Act
    response = requests.get(f"{BASE_URL}/division", params=url_params)

    # Assert
    assert response.status_code == 500
