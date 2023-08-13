from collections import deque
g = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

def solution(g):
    q = deque([(0, 0)])
    size_col = len(g[0])
    size_row = len(g)

    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    while q:
        x, y = q.popleft()
        cur_val = g[x][y]
        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx == size_row - 1 and ny == size_col - 1:
                return cur_val + 1
            if nx >= size_row or nx < 0 or ny >= size_col or ny < 0 or g[nx][ny] == 0:
                continue

            if g[nx][ny] == 1:
                g[nx][ny] = cur_val + 1
                q.append([nx, ny])

        g[x][y] = 0

    return -1


print(solution(g))