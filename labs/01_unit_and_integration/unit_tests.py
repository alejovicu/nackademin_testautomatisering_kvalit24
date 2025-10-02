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

def test_sum_one_positive_one_negative():
      # Arrange
    possitive_value = 5
    negative_value  = -10
    expected_result = {"result": -5 }

#     # Act
    result = main.addition(possitive_value,negative_value)

#     # Assert
    assert  result == expected_result


def test_sum_one_positive_one_string_value():
    with pytest.raises(TypeError):
        main.addition(5, "aaa")
    

def test_divide_two_positive_values():
    positive_value1 = 10
    negative_value2 = 5
    expected_result = {"result": 2}

    result = main.division(positive_value1,negative_value2)

    assert result == expected_result
    

def test_divide_by_zero():
    first_value = 10
    second_value = 0

    with pytest.raises(ZeroDivisionError):
        main.division(first_value,second_value)
    