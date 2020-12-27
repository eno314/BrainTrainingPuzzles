from src.part1.maru_batsu_game import Board, Input, Turn


class TestBoard:

    def test_print_when_board_is_init(self, capfd):
        Board().print()
        out, _ = capfd.readouterr()
        assert out == '□□□\n□□□\n□□□\n\n'

    def test_check_win_when_board_is_init(self):
        board = Board()

        turn = Turn()
        assert not board.check_win(turn)

        turn.change()
        assert not board.check_win(turn)

    def test_check_win_when_rows_is_draw(self):
        board = Board()
        turn = Turn()
        board.set_turn(Input.of(0, 0), turn)
        board.set_turn(Input.of(0, 1), turn)
        board.set_turn(Input.of(1, 2), turn)
        board.set_turn(Input.of(2, 0), turn)
        board.set_turn(Input.of(2, 2), turn)
        turn.change()
        board.set_turn(Input.of(0, 2), turn)
        board.set_turn(Input.of(1, 0), turn)
        board.set_turn(Input.of(1, 1), turn)
        board.set_turn(Input.of(2, 1), turn)

        turn.change()
        assert not board.check_win(turn)

        turn.change()
        assert not board.check_win(turn)

    def test_check_win_when_maru_is_win(self):
        board = Board()
        turn = Turn()
        board.set_turn(Input.of(0, 0), turn)
        board.set_turn(Input.of(0, 1), turn)
        board.set_turn(Input.of(0, 2), turn)

        assert board.check_win(turn)

        turn.change()
        assert not board.check_win(turn)

    def test_check_win_when_batsu_is_win(self):
        board = Board()
        turn = Turn()
        turn.change()
        board.set_turn(Input.of(0, 0), turn)
        board.set_turn(Input.of(1, 1), turn)
        board.set_turn(Input.of(2, 2), turn)

        turn.change()
        assert not board.check_win(turn)

        turn.change()
        assert board.check_win(turn)

    def test_check_end_when_board_is_init(self):
        board = Board()
        assert not board.check_end()

    def test_check_end_when_board_is_not_filled(self):
        board = Board()
        turn = Turn()
        for i in range(3):
            for j in range(2):
                board.set_turn(Input.of(i, j), turn)
                turn.change()
                assert not board.check_end()

    def test_check_end_when_board_is_filled(self):
        board = Board()
        turn = Turn()
        for i in range(3):
            for j in range(3):
                board.set_turn(Input.of(i, j), turn)
                turn.change()
        assert board.check_end()
