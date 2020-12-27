from maru_batsu_game import Board, Turn, validate_input


def main():
    turn = Turn()
    board = Board()
    while True:
        board.print()
        r = validate_input(input('行番号(0 ~ 2) : '))
        c = validate_input(input('列番号(0 ~ 2) : '))
        if not board.can_set(r, c):
            print('この場所は埋まっています')
            continue

        board.set_turn(r, c, turn)

        if board.check_win(turn):
            board.print()
            print('{}の勝ち'.format(turn))
            break
        if board.check_end():
            print('引き分け')
            break

        turn.change()


if __name__ == "__main__":
    main()
