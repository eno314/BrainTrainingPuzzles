class Board:

    def __init__(self):
        self.__init_board()

    def __init_board(self):
        self.__rows = [['□'] * 3 for i in range(3)]

    def can_set(self, row: int, column: int):
        return self.__rows[row][column] == '□'

    def set_turn(self, turn: str, row: int, column: int):
        self.__rows[row][column] = turn

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.__rows[i][j], end='')
            print()
        print()

    def check_win(self, turn: str) -> bool:
        # 横方向のチェック
        for r in range(3):
            if self.__rows[r][0] == turn \
                    and self.__rows[r][1] == turn \
                    and self.__rows[r][2] == turn:
                return True
        # 縦方向のチェック
        for c in range(3):
            if self.__rows[0][c] == turn \
                    and self.__rows[1][c] == turn \
                    and self.__rows[2][c] == turn:
                return True
        # 左上から右下への斜めチェック
        if self.__rows[0][0] == turn \
                and self.__rows[1][1] == turn \
                and self.__rows[2][2] == turn:
            return True
        # 右上から左下への斜めチェック
        if self.__rows[2][0] == turn \
                and self.__rows[1][1] == turn \
                and self.__rows[0][2] == turn:
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
