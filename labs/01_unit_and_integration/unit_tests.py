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
   possitive_value = 5
   negative_value  = -10
   expected_result = {"result": -5 }

   # Act
   result = main.addition(possitive_value , negative_value)


  # Assert
   assert  result == expected_result



def test_sum_one_positive_one_string_value():
    # Arrange
    number_1 = 10
    number_2 = "b"

    # Act & Assert
    try:
        main.addition(number_1, number_2)
        assert False
    except Exception:
        assert True



def test_divide_two_positive_values():

    # Arrange
    number_1 = 10
    number_2 = 5
    expected_result = {"result": 2}

    # Act
    result = main.division (number_1, number_2)

    # Assert
    result == expected_result



def test_divide_by_zero():
    # Arrange
    number_1 = 10
    number_2 = 0

    # Act & Assert
    try:
        result = main.division(number_1, number_2)
        assert False
    except ZeroDivisionError:
        assert True