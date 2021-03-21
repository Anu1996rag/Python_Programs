"""
checks if the given sudoku is valid or not
Sudoku given is partially solved

Time Complexity : O(n^2)
Space Complexity : O(n)
"""


def is_valid_sudoku(partial_assignment):
    # to check if any of the element is not equal to 0
    def has_duplicates(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    # checks for each row and for each column
    n = len(partial_assignment)
    if any(
            has_duplicates([partial_assignment[i][j] for j in range(n)])  # checks in every row
            or has_duplicates([partial_assignment[j][i] for j in range(n)])  # checks in every column
            for i in range(n)
    ):
        return False

    # checks in each of the 3 * 3 subgrids
    grid_size = int(n ** 0.5)  # taking out the square root

    return all(
        not has_duplicates(
            [partial_assignment[a][b]
             for a in range(i * grid_size, (i + 1) * grid_size)
             for b in range(j * grid_size, (j + 1) * grid_size)
             ])
        for i in range(grid_size) for j in range(grid_size)
    )
