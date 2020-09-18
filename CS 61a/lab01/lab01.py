"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    # return x and y > 0 # You can replace this line!
    return x > 0 and y > 0

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while n > 0:
        quotient, reminder = n // 10, n % 10
        n = quotient
        sum += reminder
    return sum


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    mul = 1
    while k > 0:
        mul = mul * n
        n, k = n-1, k-1
    return mul
# 未通过 why?

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    flag = 0
    while n > 0:
        d, m = n // 10, n % 10
        n = d
        if m == 8:
            flag += 1
            if flag == 2:
                return True
        else:
            flag = 0
    return False

# 未通过 why    


