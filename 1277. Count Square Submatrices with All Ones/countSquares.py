def countSquares(matrix: list[list[int]]) -> int:
    count = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(1, n):
        for j in range(1, m):

            if matrix[i][j] == 0:

                continue

            matrix[i][j] = (
                min([matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]]) + 1
            )

    for i in range(n):
        for j in range(m):
            count += matrix[i][j]

    return count
