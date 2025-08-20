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

def test_sum_one_positive_one_negative():
    # Arrange
    possitive_value_1 = 1
    negative_value_2 = -1
    expected_result = {"result": 0 }

    # Act
    result = main.addition(possitive_value_1,negative_value_2)

    # Assert
    assert  result == expected_result

    
def test_sum_one_positive_one_string_value():
        
    possitive_value_1 = 1
    string_value_2 = 'abc'

    with pytest.raises(TypeError):
        main.addition(possitive_value_1,string_value_2)

    
def test_divide_two_positive_values():
    
    positive_value_1 = 10 
    positive_value_2 = 2
    expected_result = {'result': 5}

    result = main.division(positive_value_1,positive_value_2)
    assert result == expected_result

    
def test_divide_by_zero():
    postive_value_1 = 10
    zero_value_2 = 0
    
    with pytest.raises(ZeroDivisionError):
        main.division(postive_value_1, zero_value_2)
    
