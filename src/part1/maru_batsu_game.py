from typing import List


def print_board(rows: List[List[str]]):
    for i in range(3):
        for j in range(3):
            print(rows[i][j], end='')
        print()
    print()


def init_board() -> List[List[str]]:
    rows = [['□'] * 3 for i in range(3)]
    return rows
