import main

#hej 

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
    possitive_value = 4
    negative_value  = -3
    expected_result = {"result": 1 }

    # Act
    result = main.addition( possitive_value , negative_value )

    # Assert
    assert  result == expected_result



# def test_sum_one_positive_one_string_value():


# def test_divide_two_positive_values():


# def test_divide_by_zero():