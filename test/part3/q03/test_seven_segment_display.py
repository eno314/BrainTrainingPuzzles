from src.part3.q03.seven_segment_display import LIGHTING_DICT, calc, count_appearing_number_of, count_lighting_of
import pytest


class TestCountLightingOf:

    def test_ok(self):
        for number in LIGHTING_DICT:
            assert count_lighting_of(number) == LIGHTING_DICT[number]

    def test_when_number_less_then_0(self):
        with pytest.raises(ValueError):
            count_lighting_of(-1)

    def test_when_number_greater_then_9(self):
        with pytest.raises(ValueError):
            count_lighting_of(10)


class TestCalc:

    def test(self):
        assert calc(718) == 42

    def test_when_number_is_less_than_0(self):
        with pytest.raises(ValueError):
            calc(-1)

    def test_when_number_is_less_than_10(self):
        for number in LIGHTING_DICT:
            assert calc(number) == LIGHTING_DICT[number]


class TestCountAppearingNumberOf:

    @pytest.mark.parametrize('number, expected', [
        (718, 4),
        (100, 5),
        (123456, 9)
    ])
    def test(self, number, expected):
        assert count_appearing_number_of(number) == expected
