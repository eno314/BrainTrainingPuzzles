from dataclasses import dataclass


@dataclass(frozen=True)
class Input:

    VALID_VALUES = ['0', '1', '2']

    __row: str
    __column: str

    @property
    def row(self):
        return int(self.__row)

    @property
    def column(self):
        return int(self.__column)

    def is_valid(self) -> bool:
        if (self.__row not in self.VALID_VALUES):
            return False
        if (self.__column not in self.VALID_VALUES):
            return False
        return True

    @staticmethod
    def load() -> 'Input':
        r = input('行番号(0 ~ 2) : ')
        c = input('列番号(0 ~ 2) : ')
        return Input(r, c)

    @staticmethod
    def of(row: int, column: int) -> 'Input':
        return Input(str(row), str(column))


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

    def can_set(self, input: Input):
        return self.__rows[input.row][input.column] == self.EMPTY

    def set_turn(self, input: Input, turn: Turn):
        self.__rows[input.row][input.column] = str(turn)

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
                if (self.can_set(Input.of(r, c))):
                    return False
        return True
