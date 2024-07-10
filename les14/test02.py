
def is_prime(p):
    """
    check the num - P for  simplicity using finding the reminder of the division in the range [2, p].
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    """
    for i in range(2, p):
        if not p % i:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)