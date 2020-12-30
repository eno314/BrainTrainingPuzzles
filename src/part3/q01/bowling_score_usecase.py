from src.part3.q01.bowling_score import BowlingScore
from typing import List


class BowlingScoreUsecase:

    def calculate(self, all_points: List[List[int]]) -> int:
        if len(all_points) != 10:
            raise ValueError('all points size should be 10.')
        score = BowlingScore()
        for points in all_points:
            score.add_frame_result(points)
        return score.total()
