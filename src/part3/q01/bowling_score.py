from functools import total_ordering


from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class BowlingFrameScore:

    __points: List[int]

    def total(self) -> int:
        """
        フレームの合計スコアを返す
        >>> score = BowlingFrameScore([1, 2])
        >>> score.total()
        3
        """
        return sum(self.__points)

    def is_strike(self) -> bool:
        """
        ストライクかどうか判定する
        >>> BowlingFrameScore([1, 2]).is_strike()
        False
        >>> BowlingFrameScore([8, 2]).is_strike()
        False
        >>> BowlingFrameScore([10]).is_strike()
        True
        """
        return self.__points[0] == 10

    def is_spare(self) -> bool:
        """
        スペアかどうか判定する
        >>> BowlingFrameScore([1, 2]).is_spare()
        False
        >>> BowlingFrameScore([8, 2]).is_spare()
        True
        >>> BowlingFrameScore([10]).is_spare()
        False
        """
        if self.is_strike():
            return False
        return self.__points[0] + self.__points[1] == 10

    def add_point(self, point: int):
        self.__points.append(point)


class BowlingScore:

    def __init__(self):
        self.__frame_scores: List[BowlingFrameScore] = []

    def total(self) -> int:
        return sum([
            frame_score.total()
            for frame_score in self.__frame_scores
        ])

    def add_frame_result(self, points: List[int]):
        self.__add_points_to_current(points)
        self.__add_previous_frame_score_if_need(points)

    def __add_points_to_current(self, points: List[int]):
        self.__frame_scores.append(BowlingFrameScore(points))

    def __add_previous_frame_score_if_need(self, points: List[int]):
        previous_index = len(self.__frame_scores) - 2
        if previous_index < 0:
            return
        previous_score = self.__frame_scores[previous_index]
        if previous_score.is_spare():
            previous_score.add_point(points[0])
        if previous_score.is_strike():
            previous_score.add_point(points[0])
            if (len(points) > 1):
                previous_score.add_point(points[1])
            if previous_index < 1:
                return
            more_previous_score = self.__frame_scores[previous_index - 1]
            if more_previous_score.is_strike():
                more_previous_score.add_point(points[0])
