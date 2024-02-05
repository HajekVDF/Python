
def add_int(m, n):
    """ Returns the sum of two positive integers

    Usage examples:
    >>> add_int(5, 6)
    11
    >>> add_int(125, 34)
    159

    Function accepts only positive numbers:
    >>> add_int(5, -3)
    Traceback (most recent call last):
    ValueError: m and n need to be positive integers

    Function accepts whole number floats:
    >>> add_int(5.0, 3.0)
    8
    >>> add_int(5.1, 3.5)
    Traceback (most recent call last):
    ValueError: m and n need to be whole numbers
    
    """
    import math
    if m < 0 or n < 0:
        raise ValueError("m and n need to be positive integers")
    if math.floor(m) != m or math.floor(n) != n:
        raise ValueError("m and n need to be whole numbers")

    return int(m+n)




if __name__ == "__main__":
    import doctest
    doctest.testmod()