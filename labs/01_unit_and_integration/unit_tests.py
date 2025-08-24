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
    assert expected_result == result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    # Arrange
    a = 10
    b = -15
    expected_result = {"result": -5}

    # Act
    result = main.addition(a, b)

    # Assert
    assert expected_result == result


def test_sum_one_positive_one_string_value():
    # Arrange
    a = 10
    b = "Hello, World"
    with pytest.raises(TypeError):
        main.addition(a, b)


def test_divide_two_positive_values():
    # Arrange
    a = 10
    b = 2
    expected_result = {"result": 5.0}

    # Act
    result = main.division(a, b)

    # Assert
    assert expected_result == result


def test_divide_by_zero():
    # Arrange
    with pytest.raises(ZeroDivisionError):
        main.division(10, 0)
