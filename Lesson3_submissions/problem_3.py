def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Assumption: All array elements are positive
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return None

    for input in input_list:  # Verifies the assumption to deal with only non-negative numbers
        if input < 0 or input > 9:
            return None

    sorted_list = merge_sort(input_list)

    num1 = get_alternate_places(0,sorted_list)
    num2 = get_alternate_places(1,sorted_list)

    return [num1, num2]


def get_alternate_places(index, arr):
    '''
    Returns a number composed of every alternate entries in arr starting from index
    :param index: starting index (integer)
    :param arr: list of integers
    :return: Integer composed of every alternate entries in arr starting from index
    '''
    runner = index
    result_list = []
    while runner <= len(arr)-1:
        result_list.append(arr[runner])
        runner += 2

    # reverse the list to get the max value, convert each entry to str to join and cast it to integer
    return int(''.join(map(lambda x: str(x), result_list[::-1])))


def merge_sort(arr):
    '''
    Sorts the input list using merge sort
    :param input_list: list of integers
    :return: sorted list of integers
    '''
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])

    return merge(arr1, arr2)

def merge(arr1, arr2):
    '''
    Helper function for merge sort
    :param arr1: list of integers
    :param arr2: list of integers
    :return: merged & sorted ist of integers
    '''
    left_pointer = 0
    right_pointer = 0
    res = []
    while left_pointer < len(arr1) and right_pointer < len(arr2):
        if arr1[left_pointer] < arr2[right_pointer]:
            res.append(arr1[left_pointer])
            left_pointer += 1

        else:
            res.append(arr2[right_pointer])
            right_pointer += 1

    res += arr1[left_pointer:]  # Easier to ask forgiveness than permission
    res += arr2[right_pointer:]

    return res

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if solution:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    else:
        # Solution is None
        if not output and not solution:
            print("Pass")

        else:
            print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[1,2,1,2,1,1,1],[2111,211]]
test_case4 = [[0,0,0,0,0,0], [0,0]]
test_case5 = [[-1,2,4,5,3,3],None]
test_case6 = [[9,10,1,2,3,4,5], None]
test_case7 = [[],None]

test_function(test_case2)
test_function(test_case3)
test_function(test_case4)
test_function(test_case5)
test_function(test_case6)
test_function(test_case7)