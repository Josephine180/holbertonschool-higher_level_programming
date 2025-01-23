#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers.
    The function `add_integer` takes two arguments (a and b),
    and returns their sum, casting any floats to integers.
    Parameters:
    a (int, float): The first number to add.
    b (int, float): The second number to add.
    Returns:
    int: The sum of a and b, both converted to integers if they are floats.
    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (a + b)
