from enum import Enum
from typing import List, Tuple
import random
import sys


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


class MazeResolver:

    DIRECTIONS = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    def __init__(self, aMaze: List[List[Point]]):
        self.__maze = aMaze

    def find_start(self) -> Tuple[int, int]:
        """return start position of maze
        >>> maze_resolver = MazeResolver(maze)
        >>> maze_resolver.find_start()
        (1, 1)

        if start is not found then return None
        >>> maze_resolver = MazeResolver([])
        >>> maze_resolver.find_start()

        """
        for i in range(len(self.__maze)):
            for j in range(len(self.__maze[i])):
                if self.__maze[i][j] == Point.S:
                    return (i, j)
        return None

    def random(self):
        """
        go to goal by random
        """
        x, y = self.find_start()
        while not self.__is_goal_position(x, y):
            nx, ny = self.__next_position_by_random(x, y)
            if self.__can_go_to(nx, ny):
                x = nx
                y = ny
                print([x, y])

    def __next_position_by_random(self, x: int, y: int) -> Tuple[int, int]:
        move = random.choice(self.DIRECTIONS)
        return x + move[0], y + move[1]

    def right_hand(self):
        """
        go to goal by right hand method
        """
        x, y = self.find_start()
        dir = 0
        while not self.__is_goal_position(x, y):
            move = self.DIRECTIONS[(dir + 1) % 4]
            if self.__can_go_to(x + move[0], y + move[1]):
                dir = (dir + 1) % 4
                x += move[0]
                y += move[1]
                print([x, y])
            else:
                dir = (dir + 3) % 4

    def depth_first(self) -> int:
        """
        search mini move to go to goal by depth first search.
        >>> maze_resolver = MazeResolver(maze)
        >>> maze_resolver.depth_first()
        11
        """
        start_x, start_y = self.find_start()
        start_log = [[start_x, start_y]]
        return self.__search_by_depth_first(start_log)

    def __search_by_depth_first(self, log: List[List[int]]) -> int:
        last_x, last_y = log[-1]
        if self.__is_goal_position(last_x, last_y):
            # ゴールしたら深さを返す
            return len(log) - 1

        # 深さとして十分な大きな値をセット
        depth = [sys.maxsize]
        for move in self.DIRECTIONS:
            next = [last_x + move[0], last_y + move[1]]
            if self.__can_go_to(next[0], next[1]):
                if next not in log:
                    # 過去に移動してない場所であれば移動して、再検索
                    log.append(next)
                    depth.append(self.__search_by_depth_first(log))
                    # 探索が終わったら戻る
                    log.pop(-1)
        return min(depth)

    def __can_go_to(self, x: int, y: int) -> bool:
        return self.__maze[x][y] != Point.W

    def __is_goal_position(self, x: int, y: int) -> bool:
        return self.__maze[x][y] == Point.G
