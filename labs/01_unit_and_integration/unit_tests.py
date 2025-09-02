import pytest
import main


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
    possitive_value = 18
    negative_value = -5
    expected_result = {"result": 13}

    # Act
    result = main.addition(possitive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # Arrange
    possitive_value = 20
    string_value = "nimmi"
    # expected_result = {"result": "Invalid input"}
    with pytest.raises(TypeError):
        main.addition(possitive_value, string_value)


def test_divide_two_positive_values():
    # Arrange
    possitive_value_1 = 50
    possitive_value_2 = 5
    expected_result = {"result": 10}

    # Act
    result = main.division(possitive_value_1, possitive_value_2)

    # Assert
    assert result == expected_result


def test_divide_by_zero():
    # Arrange
    possitive_value = 15
    zero_value = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        main.division(possitive_value, zero_value)
