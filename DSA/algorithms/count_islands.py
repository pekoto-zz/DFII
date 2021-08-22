from typing import List


def count_islands(matrix: List[List[int]]) -> int:
    """Given a matrix, count the number of islands, represented by 1.

    matrix = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]

    This is essentially depth-first searching a matrix.

    1. For each space, if it's a 1...
    2. Increment the island count
    3. dfs from that position:
        3.1 Check if we're out of range or at 0 (non-island).
        3.2 Mark plot as visited -- set to 0.
        3.3 dfs the offsets.

    Time: O(n*m)
    Space: O(1) -- if we can't mutate the input matrix, we could use a boolean
                array to keep track of what we visited.

    :param matrix: The matrix to search.
    :return: The number of islands.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    num_of_islands = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                num_of_islands += 1
                _dfs(matrix, row, col)

    return num_of_islands


def _dfs(matrix: List[List[int]], row: int, col: int) -> None:
    """dfs the matrix from (row,col).

    :param matrix: The input matrix.
    :param row: The row.
    :param col: The col.
    """
    if _out_of_range(matrix, row, col):
        return

    if matrix[row][col] == 0:
        return

    matrix[row][col] = 0

    _dfs(matrix, row+1, col)
    _dfs(matrix, row-1, col)
    _dfs(matrix, row, col+1)
    _dfs(matrix, row, col-1)


def _out_of_range(matrix: List[List[int]], row: int, col: int) -> bool:
    """Check if the row/col is out of range."""
    # Check if out of range
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])
