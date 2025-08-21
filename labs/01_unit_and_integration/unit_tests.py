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
    assert  result == expected_result


# Lab tasks

## Complete the following tests

def test_sum_one_positive_one_negative():
    # Arrange
    positive_value = 4
    negative_value  = -2
    expected_result = {"result": 2 }

    # Act
    result = main.addition( positive_value , negative_value )

    # Assert
    assert  result == expected_result

def test_sum_one_positive_one_string_value():
    # Arrange
    positive_value = 5
    string_value = "3"
    expected_result = {"result": 8}

    # Act
    result = main.addition(positive_value, int(string_value))

    # Assert 
    assert result == expected_result

def test_divide_two_positive_values():
    # Arrange
    first_positive_value = 9
    second_positive_value = 3
    expected_result = {"result": 3}

    # Act
    result = main.division(first_positive_value, second_positive_value)

    # Assert
    assert result == expected_result


def test_divide_by_zero():
    # Arrange
    positive_value = 8
    zero_value = 0
    expected_error = ZeroDivisionError

    # Assert
    with pytest.raises(expected_error):
        main.division(positive_value, zero_value)