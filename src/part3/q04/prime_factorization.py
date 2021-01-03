import math
from typing import List


def prime_factorization_of(number: int) -> List[int]:
    result = []
    tmp = number
    min_prime_factor = min_prime_factor_of(number)
    if min_prime_factor == number:
        return result
    while True:
        result.append(min_prime_factor)
        if tmp == min_prime_factor:
            break
        tmp = int(tmp / min_prime_factor)
        min_prime_factor = min_prime_factor_of(tmp)
    return result


def min_prime_factor_of(number: int) -> int:
    if number < 2:
        raise ValueError('number should be greater than 1.')
    max_range = int(math.sqrt(number))
    for i in range(2, max_range + 1):
        if number % i == 0:
            return i
    return number
