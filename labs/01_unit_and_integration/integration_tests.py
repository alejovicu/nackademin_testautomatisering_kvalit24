import requests

BASE_URL = "http://127.0.0.1:8000"

def test_addition():
    # Arrange
    value_1 = 10
    value_2  = 5
    url_params = {"a": value_1, "b": value_2}
    expected_result = {"result": 15}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result



def test_subtraction():
    # Arrange
    value_1 = 2
    negative_value  = 3
    url_params = {"a": value_1, "b": negative_value}
    expected_result = {"result": -1}

    # Act
    response = requests.get(f"{BASE_URL}/subtraction", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result



def test_sum_one_positive_one_negative():
    possitive_value = 20
    negative_value  = -10
    url_params = {"a": possitive_value, "b": negative_value}
    expected_result = {"result": 10}

    # Act
    response = requests.get(f"{BASE_URL}/addition", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_sum_one_positive_one_string_value():
        value_1 = 5
        value_2  = "hej"
        url_params = {"a": value_1, "b": value_2}

        # Act
        response = requests.get(f"{BASE_URL}/addition", params=url_params)

        # Assert
        assert response.status_code == 422


def test_divide_two_positive_values():
    # Arrange
    positive_value1 = 6
    positive_value2 = 3
    url_params = {"a": positive_value1, "b": positive_value2}
    expected_result = {"result": 2.0}

    # Act
    response = requests.get(f"{BASE_URL}/division", params=url_params)

    # Assert
    assert response.status_code == 200
    assert response.json() == expected_result


def test_divide_by_zero():
        # Arrange
        positive_value1 = 6
        zero_value = 0
        url_params = {"a": positive_value1, "b": zero_value}

        # Act
        response = requests.get(f"{BASE_URL}/division", params=url_params)

        # Assert
        assert response.status_code == 500