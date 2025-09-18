import main
import pytest


def test_sum_two_positives():
    # Arrange
    a = 1
    b = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(a, b)

    # Assert
    assert result == expected_result


# Lab tasks

## Complete the following tests ***COMPLETED***


def test_sum_one_positive_one_negative():
    #     # Arrange
    a = 1
    b = 1
    expected_result = {"result": 0}
    #     # Act
    result = main.substraction(a, b)
    #     # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    #     # Arrange
    a = 1
    b = "string"
    #     # Act and raises Typerror
    with pytest.raises(TypeError, match="unsupported operand type"):
        main.substraction(a, b)


def test_divide_two_positive_values():
    #     # Arrange
    a = 1
    b = 1
    expected_result = {"result": 1}
    #     # Act
    result = main.division(a, b)
    #     # Assert
    assert result == expected_result


def test_divide_by_zero():
    # Arrange
    a = 1
    b = 0
    #     # Act and raises a zerodivisionerror.
    with pytest.raises(ZeroDivisionError):
        main.division(a, b)
