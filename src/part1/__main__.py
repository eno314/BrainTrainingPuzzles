from maru_batsu_game import init_board, print_board, validate_input, check_end, check_win


def main():
    turn = '○'
    rows = init_board()
    while True:
        print_board(rows)
        r = validate_input(input('行番号(0 ~ 2) : '))
        c = validate_input(input('列番号(0 ~ 2) : '))
        if rows[r][c] != '□':
            print('この場所は埋まっています')
            continue
        rows[r][c] = turn

        if check_win(rows, turn):
            print_board(rows)
            print(turn + 'の勝ち')
            break
        if check_end(rows):
            print('引き分け')
            break

        if turn == '○':
            turn = '×'
        else:
            turn = '○'


if __name__ == "__main__":
    main()
