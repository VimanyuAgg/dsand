def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not input_list or len(input_list) < 1:
        return input_list

    low = 0
    mid = 0
    hi = len(input_list) -1
    while mid <= hi:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1

        else:
            input_list[mid], input_list[hi] = input_list[hi], input_list[mid]
            hi -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0,0,0,0])
test_function([1,0,1,1])