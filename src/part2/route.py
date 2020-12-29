import functools


def search_1(w, h) -> int:
    """
    search route
    >>> m = search_1(2, 3)
    >>> n = search_1(4, 2)
    >>> m * n
    12
    """
    if w == 1 and h == 1:
        # 到着したらカウント
        return 1

    cnt = 0
    if w > 1:
        # 右方向に動ければ移動
        cnt += search_1(w - 1, h)
    if h > 1:
        # 上方向に動ければ移動
        cnt += search_1(w, h - 1)
    return cnt


class Search2:

    def __init__(self, w: int, h: int, first_score: int):
        self.__w = w
        self.__h = h
        self.__route = [[0] * h for i in range(w)]
        self.__route[0][0] = first_score

    def search(self, x, y) -> int:
        """
        search route to convenience store from home
        >>> n = Search2(2, 3, 1).search(1, 0)
        >>> n
        3

        search route to workplace from convenience store
        >>> Search2(4, 2, n).search(1, 0)
        12
        """
        if x >= self.__w:
            return self.search(0, y + 1)
        if y >= self.__h:
            return self.__route[self.__w - 1][self.__h - 1]
        if y > 0:
            # 下からのルート
            self.__route[x][y] += self.__route[x][y - 1]
        if x > 0:
            # 左からのルート
            self.__route[x][y] += self.__route[x - 1][y]
        return self.search(x + 1, y)


def nPr(n: int, r: int) -> int:
    """
    when 3P3 then return 6
    >>> nPr(3, 3)
    6
    """
    result = 1
    for i in range(r):
        result *= (n - i)
    return result


def nCr_by_recursion(n: int, r: int) -> int:
    """nCr by recursion
    >>> nCr_by_recursion(3, 2)
    3
    """
    if (r == 0) or (r == n):
        return 1
    return nCr_by_recursion(n - 1, r - 1) + nCr_by_recursion(n - 1, r)


def nCr_by_loop(n: int, r: int) -> int:
    """nCr by loop
    >>> nCr_by_loop(4, 2)
    6
    """
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result


@functools.lru_cache(maxsize=1000)
def nCr_by_cache(n: int, r: int) -> int:
    """nCr by cache
    >>> nCr_by_cache(10, 5)
    252
    """
    if (r == 0) or (r == n):
        return 1
    return nCr_by_cache(n - 1, r - 1) + nCr_by_cache(n - 1, r)
