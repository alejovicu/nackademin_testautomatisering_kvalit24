import main
import pytest

#def test_sum_two_positives():
    # Arrange
    #possitive_value_1 = 1
    #ossitive_value_2 = 4
    #expected_result = {"result": 5 }

    # Act
    #result = main.addition(possitive_value_1,possitive_value_2)

    # Assert
    #assert  result == expected_result

#Pass Tests

def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(possitive_value_1, possitive_value_2)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_negative():
    # Arrange
    possitive_value = 10
    negative_value = -3
    expected_result = {"result": 7}

    # Act
    result = main.addition(possitive_value, negative_value)

    # Assert
    assert result == expected_result


def test_divide_two_positive_values():
    # Arrange
    value_1 = 10
    value_2 = 2
    expected_result = {"result": 5}

    # Act
    result = main.division(value_1, value_2)

    # Assert
    assert result == expected_result


#Fail Tests

def test_sum_one_positive_one_string_value():
    value_1 = 5
    value_2 = "abc"

    with pytest.raises(TypeError):
        main.addition(value_1, value_2)



def test_divide_by_zero():
    # Arrange
    value_1 = 10
    value_2 = 0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):  # Expect ZeroDivisionError for division by zero
        main.division(value_1, value_2)

# Lab tasks

## Complete the following tests

# def test_sum_one_positive_one_negative():
#     # Arrange
#     possitive_value = **
#     negative_value  = **
#     expected_result = {"result": ** }

#     # Act
#     result = main.sum( ** , ** )

#     # Assert
#     assert  result == expected_result



# def test_sum_one_positive_one_string_value():


# def test_divide_two_positive_values():


# def test_divide_by_zero():