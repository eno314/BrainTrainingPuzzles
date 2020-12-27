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


def validate_input(input: str) -> int:
    if (input not in ['0', '1', '2']):
        raise ValueError
    return int(input)


def check_win(rows: List[List[str]], turn: str) -> bool:
    # 横方向のチェック
    for r in range(3):
        if rows[r][0] == turn \
                and rows[r][1] == turn \
                and rows[r][2] == turn:
            return True
    # 縦方向のチェック
    for c in range(3):
        if rows[0][c] == turn \
                and rows[1][c] == turn \
                and rows[2][c] == turn:
            return True
    # 左上から右下への斜めチェック
    if rows[0][0] == turn \
            and rows[1][1] == turn \
            and rows[2][2] == turn:
        return True
    # 右上から左下への斜めチェック
    if rows[2][0] == turn \
            and rows[1][1] == turn \
            and rows[0][2] == turn:
        return True
    return False


def check_end(rows: List[List[str]]) -> bool:
    for r in range(3):
        for c in range(3):
            if (rows[r][c] == '□'):
                return False
    return True
