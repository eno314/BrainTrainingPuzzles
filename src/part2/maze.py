from enum import Enum
from typing import List, Tuple


class Point(Enum):
    P = 0  # 通路
    S = 1  # スタート
    G = 2  # ゴール
    W = 9  # 壁


maze = [
    [Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W],
    [Point.W, Point.S, Point.P, Point.P, Point.W, Point.W, Point.P, Point.W, Point.W],
    [Point.W, Point.P, Point.W, Point.W, Point.P, Point.P, Point.P, Point.P, Point.W],
    [Point.W, Point.P, Point.P, Point.P, Point.P, Point.W, Point.W, Point.W, Point.W],
    [Point.W, Point.W, Point.P, Point.W, Point.P, Point.W, Point.P, Point.G, Point.W],
    [Point.W, Point.P, Point.P, Point.W, Point.P, Point.P, Point.P, Point.W, Point.W],
    [Point.W, Point.P, Point.W, Point.P, Point.P, Point.W, Point.P, Point.P, Point.W],
    [Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W, Point.W],
]


def find_start(aMaze: List[List[Point]]) -> Tuple[int, int]:
    """return start position of maze
    >>> find_start(maze)
    (1, 1)

    if start is not found then return None
    >>> find_start([])

    """
    for i in range(len(aMaze)):
        for j in range(len(aMaze[i])):
            if aMaze[i][j] == Point.S:
                return (i, j)
    return None
