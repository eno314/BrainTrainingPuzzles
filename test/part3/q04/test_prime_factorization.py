from typing import List
from src.part3.q04.prime_factorization import min_prime_factor_of, prime_factorization_of
import pytest


class TestMinPrimeFactorOf:

    @pytest.mark.parametrize('number, expected', [
        (12, 2),
        (7, 7),
        (25, 5)
    ])
    def test_normal(self, number: int, expected: int):
        """
        引数で指定された数の最小の素因数を返す
        """
        assert min_prime_factor_of(number) == expected

    def test_when_number_is_less_then_2(self):
        """
        2より小さい値の場合はエラーを返す
        """
        with pytest.raises(ValueError):
            min_prime_factor_of(1)


class TestPrimeFactorizationOf:

    @pytest.mark.parametrize('number, expected', [
        (7, []),
        (4, [2, 2]),
        (6, [2, 3]),
        (12, [2, 2, 3]),
        (210, [2, 3, 5, 7]),
        (123456789, [3, 3, 3607, 3803]),
    ])
    def test_normal(self, number: int, expected: List[int]):
        """
        引数で指定された数を素因数分解して、リストで返す
        """
        assert prime_factorization_of(number) == expected

    def test_when_number_is_less_then_2(self):
        """
        2より小さい値の場合はエラーを返す
        """
        with pytest.raises(ValueError):
            prime_factorization_of(1)
