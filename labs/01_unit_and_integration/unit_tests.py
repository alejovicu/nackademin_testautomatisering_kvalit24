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
    assert result == expected_result


# Lab tasks

## Complete the following tests
def test_sum_one_positive_one_negative():
    # Arrange
    positive_value = 5
    negative_value  = -2
    expected_result = {"result": 3}

    # Act
    result = main.addition(positive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # Arrange
    positive_value = 5
    string_value = "Hello"

    with pytest.raises(TypeError):
        main.addition(positive_value, string_value)


def test_divide_two_positive_values():
    first_positive_value = 10
    second_positive_value = 2
    excepted_result = {"result": 5}

    result = main.division(first_positive_value, second_positive_value)

    assert result == excepted_result


def test_divide_by_zero():
    first_positive_value = 10
    second_postive_value = 0

    with pytest.raises(ZeroDivisionError):
        main.division(first_positive_value, second_postive_value)
