
def is_prime(p):
    """
    check the num - P for  simplicity using finding the reminder of the division in the range [2, p].
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
     ...
    TypeError: The number P must be an integer type.
    >>> is_prime(1)
    Traceback (most recent call last):
     ...
    ValueError: The number P must be greater than 1.
    >>> is_prime(-99)
    Traceback (most recent call last):
     ...
    ValueError: The number P must be greater than 1.
    >>> is_prime(100_000_001)
    if the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    if the number P is prime, the check may take a long time. Working...
    True
    """

    if not isinstance(p, int):
        raise TypeError(f'The number P must be an integer type.')
    if p < 2:
        raise ValueError(f'The number P must be greater than 1.')
    if p > 100000000:
        print(f'if the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if not p % i:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()