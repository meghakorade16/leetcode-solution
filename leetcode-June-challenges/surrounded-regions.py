def dfs(board, i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
        return
    board[i][j] = 'T'
    list = [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
    for x, y in list:
        dfs(board, x, y)


def solve(board) -> None:
    m, n = len(board), len(board[0])
    for i in range(0, m):
        dfs(board, i, 0)
        dfs(board, i, n - 1)

    for j in range(0, n):
        dfs(board, 0, j)
        dfs(board, m - 1, j)

    for i in range(m):
        for j in range(n):
            if board[i][j] != 'T':
                board[i][j] = 'X'
            else:
                board[i][j] = 'O'


if __name__ == '__main__':
    list = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solve(list)
    print(list)
