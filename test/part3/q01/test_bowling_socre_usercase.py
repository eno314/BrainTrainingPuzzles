from typing import List
import pytest
from src.part3.q01.bowling_score_usecase import BowlingScoreUsecase


@pytest.fixture
def usecase() -> BowlingScoreUsecase:
    return BowlingScoreUsecase()


def test_normal(usecase: BowlingScoreUsecase):
    """
    正常系
    """
    all_points = [
        [9, 1], [8, 2], [10], [5, 0], [3, 6],
        [4, 2], [7, 3], [6, 3], [10], [9, 1, 9]
    ]
    actual = usecase.calculate(all_points)
    assert actual == 137


@pytest.mark.parametrize('all_points', [
    [],
    [[10] for i in range(9)],
    [[10] for i in range(11)],
])
def test_error_when_all_points_size_is_not_10(
    usecase: BowlingScoreUsecase,
    all_points: List[List[int]]
):
    with pytest.raises(ValueError):
        usecase.calculate(all_points)


@pytest.mark.parametrize('all_points', [
    # 点数がない
    [[], [10], [10], [10], [10], [10], [10], [10], [10], [10]],
    # 点数が3つ以上ある
    [[10], [10], [10], [10], [10], [10], [10], [10], [1, 2, 3], [10]],
    # 1投目が10じゃないのに、点数が1つしか無い
    [[10], [9], [10], [10], [10], [10], [10], [10], [10], [10]],
    # 1投目が10なのに、点数が2つ以上ある
    [[10], [10], [10], [10], [10], [10], [10], [10, 0], [10], [10]],
])
def test_error_when_point_is_invalid_not_on_last(
    usecase: BowlingScoreUsecase,
    all_points: List[List[int]]
):
    with pytest.raises(ValueError):
        usecase.calculate(all_points)


@pytest.mark.parametrize('all_points', [
    # 点数がない
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], []],
    # 点数が1つしかない
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10]],
    # 点数が4つ以上ある
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [1, 2, 3, 4]],
    # 1投目が10なのに、点数が2つしかない
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 0]],
    # 1投目が10ではないが、1投目と2投目の合計が10なのに、点数が2つしかない
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [0, 10]],
    # 1投目と2投目の合計が10未満なのに、点数が3ある
    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [4, 5, 10]],
])
def test_error_when_point_is_invalid_on_last(
    usecase: BowlingScoreUsecase,
    all_points: List[List[int]]
):
    with pytest.raises(ValueError):
        usecase.calculate(all_points)


@pytest.mark.parametrize('all_points, expected', [
    ([[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]], 300),
    ([[10], [10], [10], [10], [10], [10], [10], [10], [10], [9, 1, 10]], 279),
    (
        [
            [9, 1], [8, 2], [10], [5, 0], [3, 6],
            [4, 2], [7, 3], [6, 3], [10], [9, 1, 9]
        ],
        137
    ),
])
def test_with_hint(
    usecase: BowlingScoreUsecase,
    all_points: List[List[int]],
    expected: int
):
    actual = usecase.calculate_with_hint(all_points)
    assert actual == expected
