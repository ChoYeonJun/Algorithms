from collections import deque


def solution(maps):
    cnt_lever = -1
    answer = -1

    start = []

    for i, row in enumerate(maps):
        if 'S' in row:
            start = [i, row.index('S')]
            break

    to_lever = deque([(start[0], start[1], -1)])
    len_r = len(maps)
    len_c = len(maps[0])
    d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[False for i in range(len_c)] for j in range(len_r)]

    lx, ly = 0, 0

    while to_lever:
        x, y, v = to_lever.popleft()

        v += 1

        if maps[x][y] == 'L':
            lx, ly = x, y
            cnt_lever = v
            break

        for [dx, dy] in d:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= len_r or ny < 0 or ny >= len_c:
                continue

            if maps[nx][ny] == 'X' or visited[nx][ny]:
                continue

            to_lever.append([nx, ny, v])
            visited[nx][ny] = True
    if cnt_lever == -1:
        return -1

    to_end = deque([(lx, ly, cnt_lever - 1)])
    visited = [[False for i in range(len_c)] for j in range(len_r)]

    while to_end:
        x, y, v = to_end.popleft()

        v += 1
        if maps[x][y] == 'E':
            answer = v
            break

        for [dx, dy] in d:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= len_r or ny < 0 or ny >= len_c:
                continue

            if maps[nx][ny] == 'X' or visited[nx][ny]:
                continue

            to_end.append([nx, ny, v])
            visited[nx][ny] = True

    return answer