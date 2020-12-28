import pytest
from src.part1_practice.constellation import Constellation, ConstellationSpecification
from src.part1_practice.date import Date


class TestConstellationSpecification:

    @pytest.mark.parametrize('birthday, expected', [
        (Constellation.AQUARIUS.value.firstDate, Constellation.AQUARIUS),
        (Constellation.AQUARIUS.value.lastDate, Constellation.AQUARIUS),
        (Constellation.PISCES.value.firstDate, Constellation.PISCES),
        (Constellation.PISCES.value.lastDate, Constellation.PISCES),
        (Constellation.ARIES.value.firstDate, Constellation.ARIES),
        (Constellation.ARIES.value.lastDate, Constellation.ARIES),
        (Constellation.TAURUS.value.firstDate, Constellation.TAURUS),
        (Constellation.TAURUS.value.lastDate, Constellation.TAURUS),
        (Constellation.GEMINI.value.firstDate, Constellation.GEMINI),
        (Constellation.GEMINI.value.lastDate, Constellation.GEMINI),
        (Constellation.CANCER.value.firstDate, Constellation.CANCER),
        (Constellation.CANCER.value.lastDate, Constellation.CANCER),
        (Constellation.LEO.value.firstDate, Constellation.LEO),
        (Constellation.LEO.value.lastDate, Constellation.LEO),
        (Constellation.VIRGO.value.firstDate, Constellation.VIRGO),
        (Constellation.VIRGO.value.lastDate, Constellation.VIRGO),
        (Constellation.LIBRA.value.firstDate, Constellation.LIBRA),
        (Constellation.LIBRA.value.lastDate, Constellation.LIBRA),
        (Constellation.SCORPION.value.firstDate, Constellation.SCORPION),
        (Constellation.SCORPION.value.lastDate, Constellation.SCORPION),
        (Constellation.SAGITTARIUS.value.firstDate, Constellation.SAGITTARIUS),
        (Constellation.SAGITTARIUS.value.lastDate, Constellation.SAGITTARIUS),
        (Constellation.CAPRICORN.value.firstDate, Constellation.CAPRICORN),
        (Constellation.CAPRICORN.value.lastDate, Constellation.CAPRICORN),
        (Date(12, 31), Constellation.CAPRICORN),
        (Date(1, 1), Constellation.CAPRICORN),
    ])
    def test_find_by_birthday(self, birthday: Date, expected: Constellation):
        specification = ConstellationSpecification()
        actual = specification.find_by_birthday(birthday)
        assert actual == expected

    def test_find_by_birthday_when_birthday_is_invalid(self):
        specification = ConstellationSpecification()
        with pytest.raises(ValueError):
            specification.find_by_birthday(Date(0, 0))
