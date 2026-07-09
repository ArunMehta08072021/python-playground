# Program to check if the Number is Perfect Number or not 
# A perfect number is a positive integer that equals the sum of its proper divisors (all divisors except the number itself). 
# For example, 6 is perfect because its divisors 1, 2, and 3 add up to 6. The next perfect numbers are 28, 496, and 8128.


def is_perfect_number(num):
    """
    Check if a number is a perfect number.
    A perfect number equals the sum of its proper divisors. Numbers less than 2 are not perfect.
    Args:
        num (int): A positive integer.
    Returns:
        bool: True if num is perfect, False otherwise.
    """

    if num < 2:
        return False
    
    total = 0

    # Loop to calculate the sum of its proper divisors (all divisors except the number itself).
    for i in range(1, num//2 + 1):
        if num%i == 0:
            total += i

    return total == num


n = int(input("Enter Any Positive Integer: "))

print(f"{n} is a Perfect Number." if is_perfect_number(n) else f"{n} is not a Perfect Number.")
