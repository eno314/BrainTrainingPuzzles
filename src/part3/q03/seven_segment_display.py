from functools import reduce
import operator


LIGHTING_DICT = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}


def count_appearing_number_of(number: int) -> int:
    appearing_numbers = [number]
    calc_number = number
    while True:
        calc_number = calc(calc_number)
        if calc_number in appearing_numbers:
            break
        appearing_numbers.append(calc_number)
    return len(appearing_numbers)


def calc(number: int) -> int:
    if number < 0:
        raise ValueError('number should be over 0')
    count_list = [
        count_lighting_of(int(digit_num_str))
        for digit_num_str in str(number)
    ]
    return reduce(operator.mul, count_list)


def count_lighting_of(number: int) -> int:
    if number not in LIGHTING_DICT:
        raise ValueError('number should be 0 ~ 9')
    return LIGHTING_DICT[number]
