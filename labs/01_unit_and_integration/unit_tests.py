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

def test_sum_one_positive_one_negative():
    # Arrange
    possitive_value = 10
    negative_value  = -5
    expected_result = {"result": 5 }

    # Act
    result = main.addition(possitive_value, negative_value )

    # Assert
    assert  result == expected_result



def test_sum_one_positive_one_string_value():
    # Arrange
    positive_value = 10
    string_value = "hej"

    # Act 
    try:
        main.addition(positive_value, string_value)
    # Assert
        assert False, "Expected TypeError but no error was raised"
    except TypeError:
        assert True


def test_divide_two_positive_values():
    # Arrange
    possitive_value1 = 10
    possitive_value2  = 2
    expected_result = {"result": 5 }

    # Act
    result = main.division(possitive_value1, possitive_value2 )

    # Assert
    assert  result == expected_result


def test_divide_by_zero():
    # Arrange
    positive_value1 = 10
    positive_value2 = 0

    # Act 
    try:
        main.division(positive_value1, positive_value2)
    # Assert
        assert False, "Expected ZeroDivisionError but no error was raised"
    except ZeroDivisionError:
        assert True