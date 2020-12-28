from typing import Any, List


def linear_search(data: List[Any], value: Any) -> int:
    """find value in data by linear search

    when value is found then return index
    >>> data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
    >>> linear_search(data, 40)
    7

    when value is not found then return -1
    >>> linear_search(data, 100)
    -1
    """
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1
