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
    positive_value = 10
    negative_value  = -5
    expected_result = {"result": 5 }
    result = main.addition(positive_value, negative_value)
    assert  result == expected_result



def test_sum_one_positive_one_string_value():
    #Arrange
    positive_value = 10
    string_value = '5'
    #Act
    with pytest.raises(TypeError) as excinfo:
        main.addition(positive_value, string_value)
        assert "unsupported operand type" in str(excinfo.value)
    
    
def test_divide_two_positive_values():
    positive_value1 = 25
    positive_value2 = 5
    expected_result = {"result": 5}
    
    result = main.division(positive_value1,positive_value2)
    assert result == expected_result



def test_divide_by_zero():
    positive_value1 = 25
    positive_value2 = 0    
    with pytest.raises(ZeroDivisionError):
        main.division(positive_value1,positive_value2)
    
