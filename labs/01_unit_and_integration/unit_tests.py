import main
import pytest


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
    positive_value = 25
    negative_value = -15
    expected_result = {"result": 10}

    # Act
    result = main.addition(positive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # Act and Assert
    with pytest.raises(TypeError):
        main.addition(17, "arina")


def test_divide_two_positive_values():
    # Arrange
    a = 15
    b = 5
    excpected_result = {"result": 3}

    # Act
    result = main.division(a, b)

    # Assert
    assert result == excpected_result


def test_divide_by_zero():
    # Arrange
    a = 13
    b = 0

    # Act and Assert
    with pytest.raises(ZeroDivisionError):
        main.division(a, b)
