from enum import Enum
from typing import List, Tuple
import random


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


def random_ai():
    # 進行方向の移動量
    d = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    # スタート位置をセット
    x, y = find_start(maze)
    # ゴールするまで繰り返す
    while maze[x][y] != Point.G:
        move = random.choice(d)
        if maze[x + move[0]][y + move[1]] != Point.W:
            x += move[0]
            y += move[1]
            print([x, y])
