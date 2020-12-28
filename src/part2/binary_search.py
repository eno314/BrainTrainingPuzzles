from typing import Any, List


def binary_search(sorted_data: List[Any], value: Any) -> int:
    """find value in data by binary search

    when value is found then return index
    >>> sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    >>> binary_search(sorted_data, 40)
    3

    when value is not found then return -1
    >>> binary_search(sorted_data, 0)
    -1

    when sorted_data is str list then return index
    >>> sorted_data = ['a', 'c', 'e', 'g', 'i', 'k', 'm', 'o', 'q']
    >>> binary_search(sorted_data, 'q')
    8
    >>> binary_search(sorted_data, 'b')
    -1

    """
    left = 0
    right = len(sorted_data) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_data[mid] == value:
            return mid
        if sorted_data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1
