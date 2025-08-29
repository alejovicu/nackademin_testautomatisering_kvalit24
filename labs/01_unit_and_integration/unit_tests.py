import main
import pytest

def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5 }

    # Act
    result = main.addition(possitive_value_1,possitive_value_2)

    # Assert
    assert  result == expected_result


# Lab tasks

## Complete the following tests

def test_sum_two_positives():
    # Arrange
    positive_value_1 = 1
    positive_value_2 = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(positive_value_1, positive_value_2)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_negative():
    # Arrange
    positive_value = 5
    negative_value = -2
    expected_result = {"result": 3}

    # Act
    result = main.addition(positive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    a = 5
    b = "3"

    with pytest.raises(TypeError):
        main.addition(a, b)


def test_divide_two_positive_values():
    a = 10
    b = 2
    expected_result = {"result": 5}

    result = main.division(a, b)

    assert result == expected_result


def test_divide_by_zero():
    a = 10
    b = 0

    with pytest.raises(ZeroDivisionError):
        main.division(a, b)
