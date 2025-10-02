import main


def test_sum_two_positives():
    # Arrange
    positive_value_1 = 1
    positive_value_2 = 4
    expected_result = {"result": 5}

    # Act
    result = main.addition(positive_value_1, positive_value_2)

    # Assert
    assert result == expected_result


# Lab tasks

## Complete the following tests


def test_sum_one_positive_one_negative():
    # Arrange
    positive_value = 5
    negative_value = -3
    expected_result = {"result": 2}

    # Act
    result = main.addition(positive_value, negative_value)

    # Assert
    assert result == expected_result


def test_sum_one_positive_one_string_value():
    positive_value = 5
    string_value = "5"

    try:
        main.addition(positive_value, string_value)
        assert False, "Expected a TypeError but none occurred"
    except TypeError:
        pass


def test_divide_two_positive_values():
    positive_value1 = 5
    positive_value2 = 5
    expected_result = {"result": 1}

    result = main.division(positive_value1, positive_value2)

    assert result == expected_result


def test_divide_by_zero():
    value1 = 10
    zerovalue = 0

    try:
        main.division(value1, zerovalue)
        assert False, "Expected a ZeroDivisionError but none occurred"
    except ZeroDivisionError:
        pass
