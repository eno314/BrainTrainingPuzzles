import pytest
from src.part1_practice.constellation_usecase import ConstellationUseCase
from src.part1_practice.constellation import ConstellationSpecification


@pytest.fixture
def spec() -> ConstellationSpecification:
    return ConstellationSpecification()


class TestLoadMonthOfBirthdayNormal:

    def test_when_input_is_digit_then_return_int_value(self, spec):
        usecase = ConstellationUseCase(lambda _: "1", spec)
        assert usecase.load_month_of_birthday() == 1

    def test_when_input_is_char_then_raise_ValueError(self, spec):
        usecase = ConstellationUseCase(lambda _: "a", spec)
        with pytest.raises(ValueError):
            usecase.load_month_of_birthday()

    def test_when_input_is_fraction_then_return_none(self, spec):
        usecase = ConstellationUseCase(lambda _: "1.1", spec)
        with pytest.raises(ValueError):
            usecase.load_month_of_birthday()


class TestLoadDayOfBirthdayNormal:

    def test_when_input_is_digit_then_return_int_value(self, spec):
        usecase = ConstellationUseCase(lambda _: "1", spec)
        assert usecase.load_day_of_birthday() == 1

    def test_when_input_is_char_then_return_none(self, spec):
        usecase = ConstellationUseCase(lambda _: "a", spec)
        with pytest.raises(ValueError):
            usecase.load_day_of_birthday()

    def test_when_input_is_fraction_then_return_none(self, spec):
        usecase = ConstellationUseCase(lambda _: "1.1", spec)
        with pytest.raises(ValueError):
            usecase.load_day_of_birthday()


class TestFind:

    def test_when_date_is_valid_then_return_constellation_str(self, spec):
        usecase = ConstellationUseCase(lambda _: '', spec)
        assert usecase.find(1, 1) == 'CAPRICORN'

    def test_when_date_is_invalid_then_return_none(self):
        usecase = ConstellationUseCase(lambda _: '', spec)
        with pytest.raises(ValueError):
            usecase.find(1, 0)
