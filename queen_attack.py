#!/bin/python3
from square_chess_board import Queen, ChessBoardGame, Obstacle


FILE_NAME = 'sample_file_1.txt'


def queensAttack(n, k, r_q, c_q, obstacles):
    """
        Determine how many squares the queen can attack
        Args:
            n : The number of rows and columns in the board
            k : The number of obstacles on the board
            r_q : The row number of the queen's position
            c_q : The column number of the queen's position
            obstacles : A list where each element is an array of 2 integers, the row and column of an obstacle
        Returns:
             The numbers os squares that the queen can attack from position (r_q, c_q)
        Raises:
            ValueError: Validation.
    """
    if n <= 0 or n > 10**5:
        raise ValueError('Board dimensions are not valid')
    if k < 0 or k > 10 ^ 5:
        raise ValueError('The number of obstacles is not valid')
    if [r_q, c_q] in obstacles:
        raise ValueError('There can be no obstacle in the position where the queen is')
    queen = Queen(row=r_q, column=c_q)
    game = ChessBoardGame(dimension=n)
    obs = [Obstacle(row=obs[0], column=obs[1]) for obs in obstacles]
    return game.count_valid_squares(queen=queen, obstacles=obs)


if __name__ == '__main__':
    with open(FILE_NAME, 'r') as reader:
        n, k = map(int, reader.readline().split(' '))
        r_q, c_q = map(int, reader.readline().split(' '))
        obstacles = []
        for x in range(k):
            obstacles.append([int(x) for x in reader.readline().split(' ')])
        result = queensAttack(n, k, r_q, c_q, obstacles)
        print(f"The queen is standing at position ({r_q}, {c_q}) on a {n}x{n} chessboard with {k} obstacles")
        print(f"The number of squares she can attack from that position is {result}.")
