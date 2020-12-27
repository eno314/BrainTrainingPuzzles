from maru_batsu_game import Board, validate_input


def main():
    turn = '○'
    board = Board()
    while True:
        board.print()
        r = validate_input(input('行番号(0 ~ 2) : '))
        c = validate_input(input('列番号(0 ~ 2) : '))
        if not board.can_set(r, c):
            print('この場所は埋まっています')
            continue
        board.set_turn(turn, r, c)

        if board.check_win(turn):
            board.print()
            print(turn + 'の勝ち')
            break
        if board.check_end():
            print('引き分け')
            break

        if turn == '○':
            turn = '×'
        else:
            turn = '○'


if __name__ == "__main__":
    main()
