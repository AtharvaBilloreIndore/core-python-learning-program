def is_odd(number):
    """
    Check if a number is odd.
    Parameters:
    number (int): The number to check.
    Returns:
    bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0

def is_even(number):
    """
    Check if a number is even.
    Parameters:
    number (int): The number to check.
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

def is_prime(number):
    """
    Determine if a number is a prime number.

    Parameters:
    number (int): The number to check.

    Returns:
    str: A message indicating whether the number is prime or not.
    """
    if number == 0 or number == 1:
        return f"{number} is not a prime number"
    elif number > 1:
        for i in range(2, int(number**0.5) + 1):
            if (number % i) == 0:
                return f"{number} is not a prime number"
        return f"{number} is a prime number"
    else:
        return f"{number} is not a prime number"


def cal_factorial(number):
    """
    Calculate the factorial of a non-negative integer.
    Parameters:
    number (int): The number to calculate the factorial of. Must be >= 0.
    Returns:
    int: The factorial of the number.
    Raises:
    ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def is_armstrong(number):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is an n-digit number that is equal to the sum of its digits raised 
    to the n-th power.
    Parameters:
    number (int): The number to check.
    Returns:
    bool: True if the number is an Armstrong number, False otherwise.
    """
    if number < 0:
        return False
    digits = str(number)
    num_digits = len(digits)
    total = sum(int(d) ** num_digits for d in digits)
    return total == number

