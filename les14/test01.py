
def is_prime(p):
    """
    check the num - P for  simplicity using finding the reminder of the division in the range [2, p].
    """
    for i in range(2, p):
        if not p % i:
            return False
    return True
