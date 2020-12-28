from maru_batsu_game import Board, Input, Turn


def main():
    turn = Turn()
    board = Board()
    while True:
        board.print()
        input = Input.load()
        if not input.is_valid():
            print('入力値が不正です')
            continue
        if not board.can_set(input):
            print('この場所は埋まっています')
            continue

        board.set_turn(input, turn)

        if board.check_win(turn):
            print('{}の勝ち'.format(turn))
            break
        if board.check_end():
            print('引き分け')
            break

        turn.change()
