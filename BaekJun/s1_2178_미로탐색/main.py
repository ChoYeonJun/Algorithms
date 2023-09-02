from collections import deque
n, m = map(int, input().split())

graph = []
visited = [[False for i in range(m)] for j in range(n)]
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
for _ in range(n):
    graph.append(input())

q = deque([(0, 0, 0)])
while q :
    x, y, v = q.popleft()

    if visited[x][y] :
        continue
    visited[x][y] = True
    v += 1

    if x == n-1 and y == m - 1:
        print(v)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny >= m or ny < 0:
            continue

        if graph[nx][ny] == '1' and not visited[nx][ny]:
            q.append([nx, ny, v])




