import pytest
from src.part1_practice.date import Date


class TestDateIsValid:

    @pytest.mark.parametrize("month, day", [
        (1, 1),
        (12, 31),
        (2, 29)
    ])
    def test_ok(self, month: int, day: int,):
        """
        when valid date then return True
        """
        date = Date.of(month, day)
        assert date.is_valid()

    @pytest.mark.parametrize("month", [
        (0),
        (-1),
        (13)
    ])
    def test_ng_when_month_is_invalid(self, month: int):
        """
        then return False
        """
        date = Date.of(month, 1)
        assert not date.is_valid()

    @pytest.mark.parametrize("day", [
        (0),
        (-1),
        (32)
    ])
    def test_ng_when_day_is_invalid(self, day: int):
        """
        then return False
        """
        date = Date.of(1, day)
        assert not date.is_valid()

    @pytest.mark.parametrize("month, day", [
        (2, 30),
        (4, 31),
        (6, 31),
        (9, 31),
        (11, 31),
    ])
    def test_ng_when_day_is_not_exists(self, month: int, day: int,):
        """
        then return False
        """
        date = Date.of(month, day)
        assert not date.is_valid()


class TestDateComparison:

    TARGET = Date(2, 2)

    @pytest.mark.parametrize('compared, expected', [
        (Date.of(2, 2), False),
        (Date.of(2, 3), False),
        (Date.of(3, 1), False),
        (Date.of(2, 1), True),
        (Date.of(1, 31), True),
    ])
    def test_greater_then(self, compared: Date, expected: bool):
        actual = self.TARGET > compared
        assert actual == expected

    @pytest.mark.parametrize('compared, expected', [
        (Date.of(2, 2), True),
        (Date.of(2, 3), True),
        (Date.of(3, 1), True),
        (Date.of(2, 1), False),
        (Date.of(1, 31), False),
    ])
    def test_less_equal_then(self, compared: Date, expected: bool):
        actual = self.TARGET <= compared
        assert actual == expected

    @pytest.mark.parametrize('compared, expected', [
        (Date.of(2, 2), True),
        (Date.of(2, 3), False),
        (Date.of(3, 1), False),
        (Date.of(2, 1), False),
        (Date.of(1, 31), False),
    ])
    def test_equals(self, compared: Date, expected: bool):
        actual = self.TARGET == compared
        assert actual == expected
