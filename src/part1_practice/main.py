from typing import Callable, Optional
from src.part1_practice.constellation_usecase import ConstellationUseCase
from src.part1_practice.constellation import ConstellationSpecification


def main():
    specification = ConstellationSpecification()
    usecase = ConstellationUseCase(__input_loader, specification)
    try:
        month = usecase.load_month_of_birthday()
        day = usecase.load_day_of_birthday()
        constellation = usecase.find(month, day)
        print('your constellation is : ' + constellation)
    except ValueError as e:
        print(e)


def __input_loader(message):
    return input(message)
