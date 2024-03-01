
def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    """
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)
