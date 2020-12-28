from dataclasses import dataclass
from enum import Enum
from typing import List

from .date import Date


@dataclass(frozen=True)
class ConstellationData:

    firstDate: Date
    lastDate: Date


class Constellation(Enum):
    AQUARIUS = ConstellationData(Date.of(1, 20), Date.of(2, 18))
    PISCES = ConstellationData(Date.of(2, 19), Date.of(3, 20))
    ARIES = ConstellationData(Date.of(3, 21), Date.of(4, 19))
    TAURUS = ConstellationData(Date.of(4, 20), Date.of(5, 20))
    GEMINI = ConstellationData(Date.of(5, 21), Date.of(6, 21))
    CANCER = ConstellationData(Date.of(6, 22), Date.of(7, 22))
    LEO = ConstellationData(Date.of(7, 23), Date.of(8, 22))
    VIRGO = ConstellationData(Date.of(8, 23), Date.of(9, 22))
    LIBRA = ConstellationData(Date.of(9, 23), Date.of(10, 23))
    SCORPION = ConstellationData(Date.of(10, 24), Date.of(11, 22))
    SAGITTARIUS = ConstellationData(Date.of(11, 23), Date.of(12, 21))
    CAPRICORN = ConstellationData(Date.of(12, 22), Date.of(1, 19))

    def is_match(self, birthday: Date) -> bool:
        if (self == self.CAPRICORN):
            return self.value.firstDate <= birthday <= Date(12, 31) \
                or Date(1, 1) <= birthday <= self.value.lastDate
        return self.value.firstDate <= birthday <= self.value.lastDate


class ConstellationSpecification:

    CONSTELATTIONS: List[Constellation] = (
        Constellation.AQUARIUS,
        Constellation.PISCES,
        Constellation.ARIES,
        Constellation.TAURUS,
        Constellation.GEMINI,
        Constellation.CANCER,
        Constellation.LEO,
        Constellation.VIRGO,
        Constellation.LIBRA,
        Constellation.SCORPION,
        Constellation.SAGITTARIUS,
        Constellation.CAPRICORN,
    )

    def find_by_birthday(self, birthday: Date) -> Constellation:
        for constellation in self.CONSTELATTIONS:
            if constellation.is_match(birthday):
                return constellation
        raise ValueError('invalid birthday')
