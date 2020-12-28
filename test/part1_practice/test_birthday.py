import pytest
from src.part1_practice.birthday import Birthday


class TestBirthday:

    @pytest.mark.parametrize("month, day", [
        (1, 1),
        (12, 31),
        (2, 29)
    ])
    def test_is_valid_ok(self, month: int, day: int,):
        """
        when valid date then return True
        """
        birthday = Birthday.of(month, day)
        assert birthday.is_valid()

    @pytest.mark.parametrize("month", [
        (0),
        (-1),
        (13)
    ])
    def test_is_valid_ng_when_month_is_invalid(self, month: int):
        """
        then return False
        """
        birthday = Birthday.of(month, 1)
        assert not birthday.is_valid()

    @pytest.mark.parametrize("day", [
        (0),
        (-1),
        (32)
    ])
    def test_is_valid_ng_when_day_is_invalid(self, day: int):
        """
        then return False
        """
        birthday = Birthday.of(1, day)
        assert not birthday.is_valid()

    @pytest.mark.parametrize("month, day", [
        (2, 30),
        (4, 31),
        (6, 31),
        (9, 31),
        (11, 31),
    ])
    def test_is_valid_ng_when_day_is_not_exists(self, month: int, day: int,):
        """
        then return False
        """
        birthday = Birthday.of(month, day)
        assert not birthday.is_valid()
