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

# Complete the following tests

def test_sum_one_positive_one_negative():
    # Arrange
    possitive_value = 10
    negative_value = -5
    expected_result = {"result": 5}

    # Act
    result = main.addition(possitive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # arrange
    possitive_value = 10
    string_value = "5"
    expected_result = {"result": 15}

    # act
    result = main.addition(possitive_value , int(string_value))


    # assert
    assert result == expected_result

    
# def test_divide_two_positive_values():
def test_subtract_two_positives():
    # Arrange
    positive_value_1 = 10
    positive_value_2 = 4
    expected_result = {"result": 6}

    # Act
    result = main.substraction(positive_value_1, positive_value_2)

    # Assert
    assert result == expected_result


# def test_divide_by_zero():
def test_divide_by_zero():
    # Arrange
    positive_value = 10
    zero_value = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        main.division(positive_value, zero_value)
