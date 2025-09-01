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

# Complete the following tests

def test_sum_one_positive_one_negative():
    # Arrange
    positive_value = 1
    negative_value  = -1
    expected_result = {"result": 0 }

    # Act
    result = main.addition( positive_value , negative_value  )

    # Assert
    assert  result == expected_result



def test_sum_one_positive_one_string_value():
     # Arrange
    positive_value = 1
    string_value = "1"
    with pytest.raises(TypeError):
        main.division(positive_value, string_value)

   


def test_divide_two_positive_values():
    # Arrange
    positive_value_1 = 10
    positive_value_2 = 2
    expected_result = {"result": 5 }

    # Act
    result = main.division(positive_value_1, positive_value_2)

    # Assert
    assert result == expected_result


def test_divide_by_zero():
     # Arrange
    positive_value = 1
    zero_value = 0
    with pytest.raises(ZeroDivisionError):
        main.division(positive_value, zero_value)