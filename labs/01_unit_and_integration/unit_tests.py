import pytest
import main

def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5 }

    # Act
    result = main.addition(possitive_value_1, possitive_value_2)

    # Assert
    assert result == expected_result


# Lab tasks

def test_sum_one_positive_one_negative():
    # Arrange
    a = 7
    b = -3
    expected_result = {"result": 4}

    # Act
    result = main.addition(a, b)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    # adding int + str should raise TypeError in pure Python
    with pytest.raises(TypeError):
        main.addition(1, "2")


def test_divide_two_positive_values():
    # 10 / 2 -> 5.0 (float)
    assert main.division(10, 2) == {"result": 5.0}


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        main.division(1, 0)
