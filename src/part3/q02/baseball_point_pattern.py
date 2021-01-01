
def calc_pattern_count(first_point: int, second_point: int) -> int:
    """
    野球の得点パターンを計算する
    >>> calc_pattern_count(1, 2)
    405
    >>> calc_pattern_count(7, 8)
    60733530
    """
    first_counter = calc_first_pattern_count(first_point)
    second_counter = calc_second_pattern_count(second_point)
    return first_counter * second_counter


def calc_first_pattern_count(point: int) -> int:
    """
    先攻の得点のパターン数を算出する
    >>> calc_first_pattern_count(1)
    9
    >>> calc_first_pattern_count(2)
    45
    """
    return calc_pattern_count(point, 9)


def calc_second_pattern_count(first_point: int, second_point: int) -> int:
    """
    後攻の得点パターンを算出する
    先攻が勝った場合は、先攻と同じ算出方法になる
    >>> calc_second_pattern_count(3, 2)
    45

    後攻が勝った場合
    >>> calc_second_pattern_count(1, 2)
    37
    """
    is_first_win = first_point > second_point
    if is_first_win:
        return calc_pattern_count(second_point, 9)
    else:
        # 8回までしか攻撃せずにpoint点取った
        without_9 = calc_pattern_count(second_point, 8)
        # 9回まで攻撃した場合、先攻が9回に何点取ったかでパターン数が決まる
        with_9 = sum([
            calc_pattern_count(i, 8) for i in range(first_point)
        ])
        return without_9 + with_9


def calc_pattern_count(point: int, inning: int) -> int:
    # 残り回数が1回になれば1通り
    if inning == 1:
        return 1
    counter = 0
    for i in range(point + 1):
        # 1イニングでi点取った場合を計算する
        counter += calc_pattern_count(point - i, inning - 1)
    return counter
