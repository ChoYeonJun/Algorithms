from collections import deque

def solution(board):
    answer = 0
    dict_dir = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}

    visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

    def bfs(x, y):
        global answer
        q = deque([(x, y, 'up', 0), (x, y, 'down', 0), (x, y, 'left', 0), (x, y, 'right', 0)])
        visited[x][y] = True

        while q:
            a, b, drct, value = q.popleft()
            nx, ny = a, b

            dx = dict_dir[drct][0]
            dy = dict_dir[drct][1]

            while True:
                nx += dx
                ny += dy

                # 벽에 부딛힌 경우
                if len(board) <= nx or nx < 0 or len(board[0]) <= ny or ny < 0 or board[nx][ny] == 'D':
                    nx -= dx
                    ny -= dy
                    break

            # 정해진 방향으로 움직일 수 없을 때
            if nx == a and ny == b:
                continue
            # 움직인 좌표의 값이 타겟 지점이면 return
            if board[nx][ny] == 'G':
                return value + 1
            # 움직인 좌표의 값이 방문하지 않았던 좌표라면 순회하도록 q 에 append
            if not visited[nx][ny]:
                visited[nx][ny] = True
                value += 1
                q.append([nx, ny, 'up', value])
                q.append([nx, ny, 'down', value])
                q.append([nx, ny, 'left', value])
                q.append([nx, ny, 'right', value])

        # q를 다 순회했는데 목표 지점에 도달하지 못했다면 -1 return
        return -1

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'R':
                answer = bfs(i, j)
                break

    return answer