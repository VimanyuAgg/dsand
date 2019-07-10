def sqrt(number):
    """
    Calculate the floored square root of a number in O(log n)

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError('Cannot find floored squared root of a negative number!')

    if number <= 1:
        return number

    res = 0

    left = 1
    right = number
    while left < right:
        mid = (left+right)//2
        if mid*mid == number:
            return mid
        elif mid*mid < number:
            left = mid + 1
        elif mid*mid > number:
            right = mid - 1
        res = mid

    if res * res > number:  # As we might have overshot the floor value during binary search
        return res - 1
    return res


print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")