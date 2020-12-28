from src.part2.maze import MazeResolver, maze


class TestMazeResolver:

    def test_can_go_to_goal_by_random(self):
        MazeResolver(maze).random()

    def test_can_go_to_goal_by_right_hand(self):
        MazeResolver(maze).right_hand()
