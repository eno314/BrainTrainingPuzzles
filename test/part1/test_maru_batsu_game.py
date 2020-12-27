from src.part1.maru_batsu_game import Board


class TestBoard:

    def test_print_when_board_is_init(self, capfd):
        Board().print()
        out, _ = capfd.readouterr()
        assert out == '□□□\n□□□\n□□□\n\n'

    def test_check_win_when_board_is_init(self):
        board = Board()
        assert not board.check_win('○')
        assert not board.check_win('x')

    def test_check_win_when_rows_is_draw(self):
        board = Board()

        rows = [
            ['○', '×', '○'],
            ['×', '○', '×'],
            ['×', '○', '×']
        ]

        for i in range(3):
            for j in range(3):
                board.set_turn(rows[i][j], i, j)

        assert not board.check_win('○') and not board.check_win('×')

    def test_check_win_when_maru_is_win(self):
        board = Board()

        rows = [
            ['○', '×', '○'],
            ['×', '○', '×'],
            ['○', '○', '×']
        ]

        for i in range(3):
            for j in range(3):
                board.set_turn(rows[i][j], i, j)

        assert board.check_win('○') and not board.check_win('×')

    def test_check_win_when_batsu_is_win(self):
        board = Board()

        rows = [
            ['○', '×', '○'],
            ['×', '×', '×'],
            ['○', '○', '×']
        ]

        for i in range(3):
            for j in range(3):
                board.set_turn(rows[i][j], i, j)

        assert not board.check_win('○') and board.check_win('×')

    def test_check_end_when_board_is_init(self):
        board = Board()
        assert not board.check_end()

    def test_check_end_when_board_is_not_filled(self):
        board = Board()
        for i in range(3):
            for j in range(2):
                board.set_turn('○', i, j)
                assert not board.check_end()

    def test_check_end_when_board_is_filled(self):
        board = Board()
        for i in range(3):
            for j in range(3):
                board.set_turn('○', i, j)
        assert board.check_end()
