
def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If any input is not a number.
    """
    if not (
        isinstance(x, (int, float))
        and isinstance(y, (int, float))
        and isinstance(z, (int, float))
    ):
        raise ValueError("All inputs must be numbers.")
    return x + y + z

def fun5(x, y):
    """
    Calculates x raised to the power of y.
    Args:
        x (int/float): Base number.
        y (int/float): Exponent.
    Returns:
        float: x raised to the power of y.
    Raises:
        ValueError: If inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x ** y

def fun6(x):
    """
    Calculates the factorial of a non-negative integer.
    Args:
        x (int): Non-negative integer.
    Returns:
        int: Factorial of x.
    Raises:
        ValueError: If x is negative or not an integer.
    """
    if not isinstance(x, int) or x < 0:
        raise ValueError("Input must be a non-negative integer.")
    if x == 0 or x == 1:
        return 1

    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def fun7(x, y):
    """
    Finds the maximum of two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: The larger of x and y.
    Raises:
        ValueError: If inputs are not numbers.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x if x > y else y

def fun8(x):
    """
    Checks if a number is even.
    Args:
        x (int): Integer to check.
    Returns:
        bool: True if x is even, False otherwise.
    Raises:
        ValueError: If input is not an integer.
    """
    if not isinstance(x, int):
        raise ValueError("Input must be an integer.")
    return x % 2 == 0

def fun9(x):
    """
    Calculates the square root of a number.
    Args:
        x (int/float): Non-negative number.
    Returns:
        float: Square root of x.
    Raises:
        ValueError: If input is negative or not a number.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number.")
    return x ** 0.5

# f1_op = fun1(2, 3)
# f2_op = fun2(2, 3)
# f3_op = fun3(2, 3)
# f4_op = fun4(f1_op, f2_op, f3_op)
# f5_op = fun5(2, 3)
# f6_op = fun6(5)
# f7_op = fun7(f1_op, f3_op)
# f8_op = fun8(f3_op)
# f9_op = fun9(f4_op)
