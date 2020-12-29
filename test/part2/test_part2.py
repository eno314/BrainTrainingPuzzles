from src.part2.maze import MazeResolver, maze


class TestMazeResolver:

    def test_can_go_to_goal_by_random(self):
        MazeResolver(maze).random()

    def test_can_go_to_goal_by_right_hand(self):
        MazeResolver(maze).right_hand()

    def test_depth_first_search(self):
        assert MazeResolver(maze).depth_first() == 11

    def test_breadth_first_search(self):
        assert MazeResolver(maze).breadth_first() == 11

    def test_bidirection_search(self):
        assert MazeResolver(maze).bidirection_search() == 11
