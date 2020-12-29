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
    [Point.W, Point.W, Point.W, Point.W, Point.W,
        Point.W, Point.W, Point.W, Point.W],
    [Point.W, Point.S, Point.P, Point.P, Point.W,
        Point.W, Point.P, Point.W, Point.W],
    [Point.W, Point.P, Point.W, Point.W, Point.P,
        Point.P, Point.P, Point.P, Point.W],
    [Point.W, Point.P, Point.P, Point.P, Point.P,
        Point.W, Point.W, Point.W, Point.W],
    [Point.W, Point.W, Point.P, Point.W, Point.P,
        Point.W, Point.P, Point.G, Point.W],
    [Point.W, Point.P, Point.P, Point.W, Point.P,
        Point.P, Point.P, Point.W, Point.W],
    [Point.W, Point.P, Point.W, Point.P, Point.P,
        Point.W, Point.P, Point.P, Point.W],
    [Point.W, Point.W, Point.W, Point.W, Point.W,
        Point.W, Point.W, Point.W, Point.W],
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
        return self.__find_point(Point.S)

    def find_goal(self) -> Tuple[int, int]:
        """return goal position of maze
        >>> maze_resolver = MazeResolver(maze)
        >>> maze_resolver.find_goal()
        (4, 7)

        if start is not found then return None
        >>> maze_resolver = MazeResolver([])
        >>> maze_resolver.find_goal()

        """
        return self.__find_point(Point.G)

    def __find_point(self, point: Point) -> Tuple[int, int]:
        for i in range(len(self.__maze)):
            for j in range(len(self.__maze[i])):
                if self.__maze[i][j] == point:
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
        search min move to go to goal by depth first search.
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
                    print('log  : {}, depth : {}'.format(log, depth))
                    # 探索が終わったら戻る
                    log.pop(-1)
        return min(depth)

    def breadth_first(self) -> int:
        """
        search min move to go to goal by breadth first search.
        """
        start_x, start_y = self.find_start()
        log = [[start_x, start_y]]
        queue = [[start_x, start_y, 0]]

        while len(queue) > 0:
            x, y, depth = queue.pop(0)
            for move in self.DIRECTIONS:
                next = [x + move[0], y + move[1]]
                if self.__is_goal_position(next[0], next[1]):
                    # ゴールしたら深さを返す
                    return depth + 1
                if self.__can_go_to(next[0], next[1]):
                    if next not in log:
                        # 過去に移動していない場所の場合に、ログとキューに追加
                        log.append(next)
                        queue.append([next[0], next[1], depth + 1])
                        print('log : {}, queue: {}'.format(log, queue))
        # ゴールが見つからなかった
        return -1

    def bidirection_search(self) -> int:
        start_x, start_y = self.find_start()
        log_fw, q_fw = [[start_x, start_y]], [[start_x, start_y]]
        goal_x, goal_y = self.find_goal()
        log_bw, q_bw = [[goal_x, goal_y]], [[goal_x, goal_y]]
        depth = 0
        while True:
            # スタートからゴールに向けて1段進める
            q_fw = self.__get_next(q_fw, log_fw)
            depth += 1
            print('q_fw : {}'.format(q_fw))
            if self.__check_duplicate(q_fw, q_bw):
                break

            # ゴールからスタートに向けて1段進める
            q_bw = self.__get_next(q_bw, log_bw)
            depth += 1
            print('q_bw : {}'.format(q_bw))
            if self.__check_duplicate(q_fw, q_bw):
                break
        return depth

    def __get_next(
        self,
        queue: List[List[int]],
        log: List[List[int]]
    ) -> List[List[int]]:
        result = []
        for x, y in queue:
            for move in self.DIRECTIONS:
                next = [x + move[0], y + move[1]]
                if self.__can_go_to(next[0], next[1]):
                    if next not in log:
                        log.append(next)
                        result.append(next)
        return result

    def __check_duplicate(
        self,
        fw: List[Tuple[int, int]],
        bw: List[Tuple[int, int]]
    ) -> bool:
        for position in fw:
            if position in bw:
                return True
        return False

    def __can_go_to(self, x: int, y: int) -> bool:
        return self.__maze[x][y] != Point.W

    def __is_goal_position(self, x: int, y: int) -> bool:
        return self.__maze[x][y] == Point.G
