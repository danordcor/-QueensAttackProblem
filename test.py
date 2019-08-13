import unittest

from square_chess_board import Queen, Obstacle, ChessBoardGame
from queen_attack import queensAttack


class TestQueen(unittest.TestCase):

    def test_distance_for_dimension_6(self):
        """Check the 4 distances on an 6-dimensional chess board"""
        queen = Queen(4, 4)
        right, left, above, below = queen.get_distance_for_dimension(dimension=6)
        self.assertEqual(right, 2)
        self.assertEqual(left, 3)
        self.assertEqual(above, 2)
        self.assertEqual(below, 3)

    def test_distance_for_dimension_4(self):
        """Check the 4 distances on an 4-dimensional chess board"""
        queen = Queen(1, 4)
        right, left, above, below = queen.get_distance_for_dimension(dimension=4)
        self.assertEqual(right, 0)
        self.assertEqual(left, 3)
        self.assertEqual(above, 3)
        self.assertEqual(below, 0)


class TestObstacle(unittest.TestCase):

    def test_diff_with_queen(self):
        """Check the method to get the distance between the queen and an obstacle"""
        queen = Queen(1, 4)
        obstacle_1 = Obstacle(4, 1)
        obstacle_2 = Obstacle(4, 4)
        row, column = obstacle_1.get_diff_with_queen(queen=queen)
        self.assertEqual(row, 3)
        self.assertEqual(column, -3)
        row, column = obstacle_2.get_diff_with_queen(queen=queen)
        self.assertEqual(row, 0)
        self.assertEqual(column, -3)


class TestChessBoardGame(unittest.TestCase):

    def test_count_valid_squares_in_8x8(self):
        """Test for count valid squares in 8x8 chess board"""
        game = ChessBoardGame(dimension=8)
        queen = Queen(4, 4)
        obstacles = []
        self.assertEquals(game.count_valid_squares(queen=queen, obstacles=obstacles), 27)

    def test_count_valid_squares_in_8x8_with_1_obstacle(self):
        """Test for count valid squares in 8x8 chess board, with obstacles"""
        game = ChessBoardGame(dimension=8)
        queen = Queen(4, 4)
        obstacles = [Obstacle(3, 5)]
        self.assertEquals(game.count_valid_squares(queen=queen, obstacles=obstacles), 24)

    def test_count_valid_squares_in_4x4(self):
        """Test for count valid squares in 4x4 chess board"""
        game = ChessBoardGame(dimension=4)
        queen = Queen(4, 4)
        obstacles = []
        self.assertEquals(game.count_valid_squares(queen=queen, obstacles=obstacles), 9)

    def test_count_valid_squares_in_5x5_with_3_obstacles(self):
        """Test for count valid squares in 5x5 chess board, with obstacles"""
        game = ChessBoardGame(dimension=5)
        queen = Queen(4, 3)
        obstacles = [Obstacle(5, 5), Obstacle(4, 2), Obstacle(2, 3)]
        self.assertEquals(game.count_valid_squares(queen=queen, obstacles=obstacles), 10)

    def test_count_valid_squares_in_1x1(self):
        """Test for count valid squares in 1x1 chess board"""
        game = ChessBoardGame(dimension=1)
        queen = Queen(1, 1)
        obstacles = []
        self.assertEquals(game.count_valid_squares(queen=queen, obstacles=obstacles), 0)


class TestQueenAttack(unittest.TestCase):

    def setUp(self):
        self.queens_attack = queensAttack

    def test_queens_attack(self):
        """Test for queens attack"""
        obs = []
        self.assertEquals(self.queens_attack(4, 0, 4, 4, obs), 9)
        obs = [[5, 5], [4, 2], [2, 3]]
        self.assertEquals(self.queens_attack(5, 3, 4, 3, obs), 10)
        self.assertEquals(self.queens_attack(1, 0, 1, 1, obs), 0)
        obs = [[5, 5], [4, 2], [2, 3]]
        self.assertEquals(self.queens_attack(5, 3, 1, 1, obs), 11)
        obs = [[5, 5], [4, 2], [2, 3]]
        self.assertEquals(self.queens_attack(5, 5, 4, 3, obs), 10)
        obs = [[2, 4]]
        self.assertEquals(self.queens_attack(4, 1, 4, 4, obs), 7)
        obs = []
        self.assertEquals(self.queens_attack(8, 0, 4, 4, obs), 27)
        obs = [[3, 5]]
        self.assertEquals(self.queens_attack(8, 1, 4, 4, obs), 24)
        obs = [[3, 5], [2, 6]]
        self.assertEquals(self.queens_attack(8, 1, 4, 4, obs), 24)
        obs = [[3, 5], [5, 4]]
        self.assertEquals(self.queens_attack(8, 2, 4, 4, obs), 20)

    def test_raise_obstacle_in_queen_position(self):
        """Check raise when there is an obstacle in the queen's position"""
        self.assertRaises(ValueError, self.queens_attack, 5, 3, 4, 3, [[4, 3]])

    def test_dimensions_out_of_range(self):
        """Check raise when the dimensions are out of range"""
        self.assertRaises(ValueError, self.queens_attack, -1, 1, 1, 1, [])
        self.assertRaises(ValueError, self.queens_attack, 0, 1, 1, 1, [])
        self.assertRaises(ValueError, self.queens_attack, 10**5+1, 1, 1, 1, [])

    def test_obstacles_numbers_out_of_range(self):
        """Check raise when the obstacles numbers are out of range"""
        self.assertRaises(ValueError, self.queens_attack, 1, -1, 1, 1, [])
        self.assertRaises(ValueError, self.queens_attack,  1, 10**5, 1, 1, [])


if __name__ == '__main__':
    unittest.main()
