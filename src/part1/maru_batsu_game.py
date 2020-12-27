from dataclasses import dataclass


@dataclass
class Turn:

    FIRST = '○'
    SECOND = '×'

    __current = FIRST

    def __str__(self) -> str:
        return self.__current

    def change(self):
        if self.__current == self.FIRST:
            self.__current = self.SECOND
        else:
            self.__current = self.FIRST


class Board:

    EMPTY = '□'

    def __init__(self):
        self.__init_board()

    def __init_board(self):
        self.__rows = [[self.EMPTY] * 3 for i in range(3)]

    def can_set(self, row: int, column: int):
        return self.__rows[row][column] == self.EMPTY

    def set_turn(self, row: int, column: int, turn: Turn):
        self.__rows[row][column] = str(turn)

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.__rows[i][j], end='')
            print()
        print()

    def check_win(self, turn: Turn) -> bool:
        turn_str = str(turn)
        # 横方向のチェック
        for r in range(3):
            if self.__rows[r][0] == turn_str \
                    and self.__rows[r][1] == turn_str \
                    and self.__rows[r][2] == turn_str:
                return True
        # 縦方向のチェック
        for c in range(3):
            if self.__rows[0][c] == turn_str \
                    and self.__rows[1][c] == turn_str \
                    and self.__rows[2][c] == turn_str:
                return True
        # 左上から右下への斜めチェック
        if self.__rows[0][0] == turn_str \
                and self.__rows[1][1] == turn_str \
                and self.__rows[2][2] == turn_str:
            return True
        # 右上から左下への斜めチェック
        if self.__rows[2][0] == turn_str \
                and self.__rows[1][1] == turn_str \
                and self.__rows[0][2] == turn_str:
            return True
        return False

    def check_end(self) -> bool:
        for r in range(3):
            for c in range(3):
                if (self.can_set(r, c)):
                    return False
        return True


def validate_input(input: str) -> int:
    if (input not in ['0', '1', '2']):
        raise ValueError
    return int(input)
