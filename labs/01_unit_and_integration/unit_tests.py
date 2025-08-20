import main
import pytest

def test_sum_two_positives():
    # Arrange
    positive_value_1 = 1
    positive_value_2 = 4
    expected_result = {"result": 5 }

    # Act
    result = main.addition(positive_value_1,positive_value_2)

    # Assert
    assert result == expected_result


# Lab tasks

## Complete the following tests

def test_sum_one_positive_one_negative():

    # Arrange
    positive_value_1 = 5
    negative_value_1 = -10
    expected_result = {"result": -5 }

    # Act
    result = main.addition(positive_value_1,negative_value_1)

    # Assert
    assert result == expected_result



def test_sum_one_positive_one_string_value():
    
    # Arrange
    positive_value_1 = 5
    string_value_1 = 'aa'

    # Assert
    with pytest.raises(TypeError):
        main.addition(positive_value_1, string_value_1)


def test_divide_two_positive_values():
    # Arrange
    positive_value_1 = 10
    positive_value_2 = 2
    expected_result = {"result": 5 }

    # Act
    result = main.division(positive_value_1,positive_value_2)

    # Assert
    assert result == expected_result


def test_divide_by_zero():

    # Arrange
    positive_value_1 = 5
    zero_value = 0

    # Assert
    with pytest.raises(ZeroDivisionError):
        main.division(positive_value_1, zero_value)