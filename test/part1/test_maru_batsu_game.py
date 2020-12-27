from src.part1.maru_batsu_game import check_win, init_board


class TestCheckWin:

    def test_when_rows_is_init(self):
        rows = init_board()
        assert not check_win(rows, '○') and not check_win(rows, '×')

    def test_when_rows_is_draw_then_return_False(self):
        rows = [
            ['×', '○', '×'],
            ['○', '×', '×'],
            ['○', '×', '○'],
        ]
        assert not check_win(rows, '○') and not check_win(rows, '×')

    def test_when_maru_is_win(self):
        rows = [
            ['×', '○', '×'],
            ['○', '×', '×'],
            ['○', '○', '○'],
        ]
        assert check_win(rows, '○') and not check_win(rows, '×')

    def test_when_batsu_is_win(self):
        rows = [
            ['○', '○', '×'],
            ['×', '×', '○'],
            ['×', '○', '○'],
        ]
        assert not check_win(rows, '○') and check_win(rows, '×')
