from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Date:

    __month: int
    __day: int

    def is_valid(self) -> bool:
        if self.__month < 1 or 12 < self.__month:
            return False
        if self.__day < 1 or 31 < self.__day:
            return False
        if not self.__is_exists_date():
            return False
        return True

    def __is_exists_date(self) -> bool:
        if self.__month == 2 and self.__day > 29:
            return False
        month_list_of_having_31_day = (1, 3, 5, 7, 8, 10, 12)
        if self.__month not in month_list_of_having_31_day and self.__day > 30:
            return False
        return True

    @staticmethod
    def of(month: int, day: int) -> 'Date':
        return Date(month, day)
