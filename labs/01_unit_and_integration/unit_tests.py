import main
import pytest


def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(possitive_value_1, possitive_value_2)

    # Assert
    assert result == expected_result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    #     # Arrange
    possitive_value = 3
    negative_value = -5
    expected_result = {"result": -2}

    #     # Act
    result = main.addition(possitive_value, negative_value)

    #     # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    #     # Arrange
    possitive_value = 3
    string_value = "abc"
    # expected_result = {TypeError}

    # Act & Assert
    with pytest.raises(TypeError):
        main.addition(possitive_value, string_value)


def test_divide_two_positive_values():
    #     # Arrange
    possitive_value_1 = 10
    possitive_value_2 = 5
    expected_result = {"result": 2}

    #     # Act
    result = main.division(possitive_value_1, possitive_value_2)

    #     # Assert
    assert result == expected_result


def test_divide_by_zero():
    #     # Arrange
    possitive_value_1 = 10
    possitive_value_2 = 0
    # expected_result = {"result": 0 or undefined}

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        main.division(possitive_value_1, possitive_value_2)
