import pytest

def binary_search(sorted_list, target):
    """
    Binary Search algorithm to find the index of the target value in a sorted list.

    Parameters:
    - sorted_list (list): A sorted list of integers.
    - target (int): The target value to search for.

    Returns:
    - int: The index of the target value in the list, or -1 if not found.
    """
    
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# do not modify this function call
retcode = pytest.main(['-v'])