import main

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