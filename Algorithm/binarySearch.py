# For Binary-Search items must be sorted either in ascending or in descending order
import numpy as np


def binary_search(my_list, search):
    """This function searches an value in an array using binary search algorithm    
    Args:
        my_list (list)
        search (int)
    Returns: if value is found or not
    """
    left, right = 0, len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == search:
            return f"Search Value {search} found at index {mid}"
        elif my_list[mid] > search:
            right = mid - 1
        else:
            left = mid + 1
    return f"Search value {search} not found in array!"


if __name__ == '__main__':
    try:
        nums = np.random.randint(1, 99, size=10)
        nums.sort()
        user = int(input("Enter number to search: "))
        result = binary_search(nums, user)
    except ValueError:
        print("Please enter a valid integer!")
    except Exception as err:
        print(f"Something unexpected occurred: {err}")
    else:
        print("########################################################################################")
        print(f"\t\t\t{result}")
        print("########################################################################################")
