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
    # Arrange
    positive_value = 50
    negative_value = -25
    expected_result = {"result": 25}

    # Act
    result = main.addition(positive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # Arrange
    positive_value = 50
    string_value = "Hejsan"

    # Act & Assert
    with pytest.raises(TypeError):
        main.addition(positive_value, string_value)


def test_divide_two_positive_values():
    # Arrange
    number1 = 50
    number2 = 2
    expected_result = {"result": 25}

    # Act
    result = main.division(number1, number2)

    # Assert
    assert result == expected_result


def test_divide_by_zero():
    # Arrange
    number1 = 50
    number2 = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        main.division(number1, number2)
