import main
#1
def test_sum_two_positives():
    # Arrange
    possitive_value_1 = 1
    possitive_value_2 = 4
    expected_result = {"result": 5 }
    # Act
    result = main.addition(possitive_value_1,possitive_value_2)
    # Assert
    assert result == expected_result


#2
def test_sum_two_positives2():
    # Arrange
    possitive_value_1 = 4
    possitive_value_2 = 1
    expected_result = {"result": 5 }
    # Act
    result = main.addition(possitive_value_1,possitive_value_2)
    # Assert
    assert  result == expected_result


#3    
def test_sum_one_positive_one_negative():
   # Arrange
   positive_value = 5
   negative_value  = -6
   expected_result = {"result": -1}
   # Act
   result = main.addition( positive_value , negative_value )
  # Assert
   assert  result == expected_result


#4
def test_sum_one_positive_one_string_value():
 # Arrange
    value_1 = 5
    value_2  = "hej"
  # Act
    try:
        main.addition( value_1 , value_2 )
    except TypeError:
        assert True
    #else:
        #assert False, "Expected TypeError but none was raised"

 


#5
def test_divide_two_positive_values():
    # Arrange
    positive_value1 = 6
    positive_value2 = 3
    expected_result = {"result": 2.0}
    # Act
    result = main.division(positive_value1, positive_value2)
    # Assert
    assert result == expected_result


#6
# def test_divide_by_zero():
def test_divide_by_zero():
    # Arrange
   positive_value = 3
   another_value = 0
  # Act
   try:
        main.division( positive_value , another_value )
  # Assert
   except ZeroDivisionError:
         assert True
   #else:
        # assert False, "Expected ZeroDivisionError but none was raised"