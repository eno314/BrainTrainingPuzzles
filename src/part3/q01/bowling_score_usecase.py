from src.part3.q01.bowling_score import BowlingScore
from typing import List


class BowlingScoreUsecase:

    def calculate(self, all_points: List[List[int]]) -> int:
        """
        ヒントを見ずに書いたプログラム
        """
        if len(all_points) != 10:
            raise ValueError('all points size should be 10.')
        score = BowlingScore()
        for points in all_points:
            score.add_frame_result(points)
        return score.total()

    def calculate_with_hint(self, all_points: List[List[int]]) -> int:
        """
        ヒントを見て書いたプログラム
        """
        total, next_point, next_of_next_point = 0, 0, 0
        for points in (reversed(all_points)):
            frame_point = sum(points)
            total += frame_point
            if (len(points) == 1):
                # 最終フレーム以外のストライクの場合
                total += (next_point + next_of_next_point)
                next_of_next_point = next_point
                next_point = points[0]
            else:
                if (frame_point == 10):
                    # スペアの場合
                    total += next_point
                next_point = points[0]
                next_of_next_point = points[1]
        return total
