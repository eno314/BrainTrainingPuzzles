import pytest
from src.part3.q01.bowling_score import BowlingScore


@pytest.fixture
def bowling_score() -> BowlingScore:
    return BowlingScore()


def test_neither_strike_nor_spare(bowling_score: BowlingScore):
    """
    ストライクでもスペアでもない場合、1投目と2投目の合計の値が、合計のスコアに加算される
    """
    bowling_score.add_frame_result([1, 2])
    assert bowling_score.total() == 3

    bowling_score.add_frame_result([9, 0])
    assert bowling_score.total() == 12


def test_spare(bowling_score: BowlingScore):
    """
    スペアの場合、1投目と2投目の合計の値に次の1投分の点数を加算した値が、合計のスコアに加算される
    """
    bowling_score.add_frame_result([6, 4])
    bowling_score.add_frame_result([8, 2])
    bowling_score.add_frame_result([0, 9])
    assert bowling_score.total() == 37


def test_strick(bowling_score: BowlingScore):
    """
    ストライクの場合、1投目と2投目の合計の値に次の2投分の点数を加算した値が、合計のスコアに加算される
    """
    bowling_score.add_frame_result([10])
    bowling_score.add_frame_result([10])
    bowling_score.add_frame_result([5, 4])
    assert bowling_score.total() == (25 + 19 + 9)


def test_all_strick(bowling_score: BowlingScore):
    """
    全部ストライクの場合_合計スコアは300になる
    """
    for i in range(9):
        bowling_score.add_frame_result([10])
    bowling_score.add_frame_result([10, 10, 10])
    assert bowling_score.total() == 300
