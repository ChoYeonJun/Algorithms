from collections import deque

N, L, R = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(r, c):
    m = [[r, c]]
    q = deque([(r, c)])
    total = graph[r][c]
    size = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny >= N or ny < 0 or visited[nx][ny]: continue
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R and [nx, ny] not in m:
                q.append((nx, ny))
                m.append([nx, ny])
                total += graph[nx][ny]
                size += 1

    v = total // size
    for x, y in m:
        graph[x][y] = v


cnt = 0
while True:
    visited = [[False for i in range(N)] for j in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue
            bfs(i, j)
            idx += 1
    if idx == N * N:
        break
    cnt += 1
print(cnt)