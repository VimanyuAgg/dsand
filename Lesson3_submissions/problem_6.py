def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
       return None, None

    if len(ints) == 1:
        return ints[0], ints[0]

    minimum = ints[0]
    maximum = ints[0]

    for i in ints:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i

    return minimum, maximum

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 2
t2 = []
print("Pass" if ((None, None) == get_min_max(t2)) else "Fail")

# Test Case 3
t3 = [100]
print("Pass" if ((100, 100) == get_min_max(t3)) else "Fail")

# Test Case 4
t4 = [100,-1]
print("Pass" if ((-1, 100) == get_min_max(t4)) else "Fail")

# Test Case 5
t5 = [100,100]
print("Pass" if ((100, 100) == get_min_max(t5)) else "Fail")