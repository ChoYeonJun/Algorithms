from collections import Counter


def solution(board):
    dx = [-1, -1, 1, 1, 0, 0, 1, -1]
    dy = [1, -1, 1, -1, 1, -1, 0, 0]
    points = []
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                for k in range(len(dx)):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx < 0 or nx >= size or ny < 0 or ny >= size:
                        continue
                    points.append([nx, ny])

    for point in points:
        x, y = point
        board[x][y] = 1
    answer = 0

    for row in board:
        answer += Counter(row)[0]

    return answer