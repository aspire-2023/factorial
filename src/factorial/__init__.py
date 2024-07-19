def factorial(n):
    """Return the factor of an integer number >= 0"""

    if n < 0:
        raise ValueError("number is negative")
    if n in [0, 1, 2]:
        return n
    return n * factorial(n-1)
