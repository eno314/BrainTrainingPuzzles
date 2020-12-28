from typing import Callable, Optional
from src.part1_practice.constellation import ConstellationSpecification
from src.part1_practice.date import Date


class ConstellationUseCase:

    def __init__(self,
                 input_loader: Callable[[str], str],
                 specification: ConstellationSpecification):
        self.__input_loader = input_loader
        self.__specification = specification

    def find(
            self,
            month_of_birthday: int,
            day_of_birthday: int
    ) -> Optional[str]:
        birthday = Date(month_of_birthday, day_of_birthday)
        if not birthday.is_valid():
            raise ValueError('birthday is invalid date.')
        constellation = self.__specification.find_by_birthday(birthday)
        return constellation.name

    def load_month_of_birthday(self) -> int:
        input_month = self.__input_loader('input month of birthday : ')
        return self.__validate_input_value(input_month)

    def load_day_of_birthday(self) -> int:
        input_day = self.__input_loader('input day of birthday : ')
        return self.__validate_input_value(input_day)

    def __validate_input_value(self, input_value) -> int:
        if not input_value.isdecimal():
            raise ValueError('input value is invalid.')
        return int(input_value)
