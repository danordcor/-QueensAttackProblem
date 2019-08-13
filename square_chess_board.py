class Queen:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_distance_for_dimension(self, dimension):
        """
            Determine the distance between the queen and the limits of a board
            Args:
                dimension: The width and height of a chess board
            Returns:
                A tuple with the distances between the queen and the right left, up, down
        """
        right = dimension - self.column
        left = self.column - 1
        up = dimension - self.row
        down = self.row - 1
        return right, left, up, down


class Obstacle:

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_diff_with_queen(self, queen):
        """
            Determine the difference of positions with a queen
            Args:
                queen: The queen for compare positions
            Returns:
                column difference, row difference
        """
        return queen.column - self.column, queen.row - self.row


class ChessBoardGame:

    def __init__(self, dimension):
        self.dimension = dimension

    def count_valid_squares(self, queen, obstacles):
        """
            Determine how many squares the queen can attack on the current board
            Args:
                queen: The queen in the chess board
                obstacles: A list of Obstacle instances
            Returns:
                The total squares that the queen can attack.
        """
        # Initialize all distances without obstacles
        right, left, up, down = queen.get_distance_for_dimension(dimension=self.dimension)
        right_up = min(right, up)
        right_down = min(right, down)
        left_up = min(left, down)
        left_down = min(left, up)

        # Iterate the obstacles and update the distances
        for obstacle in obstacles:
            # The orientations between the obstacle and the queen are defined
            horizontal_diff_with_queen, vertical_diff_with_queen = obstacle.get_diff_with_queen(queen=queen)
            is_right_of_queen = horizontal_diff_with_queen < 0
            is_above_of_queen = vertical_diff_with_queen < 0
            is_diagonal_of_queen = abs(vertical_diff_with_queen) == abs(horizontal_diff_with_queen)

            # If the obstacle is in the same row as the queen
            if vertical_diff_with_queen == 0:
                # Change horizontal positions
                diff = abs(horizontal_diff_with_queen) - 1
                right = self.get_min_distance(is_right_of_queen, right, diff)
                left = self.get_min_distance(not is_right_of_queen, left, diff)

            # If the obstacle is in the same column as the queen
            if horizontal_diff_with_queen == 0:
                # Change vertical positions
                diff = abs(vertical_diff_with_queen) - 1
                up = self.get_min_distance(is_above_of_queen, up, diff)
                down = self.get_min_distance(not is_above_of_queen, down, diff)

            # If the obstacle is diagonal to the queen
            if is_diagonal_of_queen:
                # Change diagonal positions
                diff = abs(vertical_diff_with_queen) - 1
                right_up = self.get_min_distance(is_right_of_queen and is_above_of_queen, right_up, diff)
                left_down = self.get_min_distance(not is_right_of_queen and is_above_of_queen, left_down, diff)
                left_up = self.get_min_distance(not is_right_of_queen and not is_above_of_queen, left_up, diff)
                right_down = self.get_min_distance(is_right_of_queen and not is_above_of_queen, right_down, diff)

        # Return the sum of all positions
        return right + left + up + down + right_up + right_down + left_up + left_down

    @staticmethod
    def get_min_distance(condition, value, new_value):
        """
            Determine the minimum distance if they have the correct alignment
            Args:
                condition: The condition for check
                value: The current value of the distance
                new_value: the possible new value of the distance
            Returns:
                The final distance between the queen and a obstacle in the chess board
        """
        return min(value, new_value) if condition else value
