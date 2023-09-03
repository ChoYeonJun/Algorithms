from collections import deque
R, C = map(int, input().split())
g = []

# bfs 순서는 q에서 처리하자
q = deque()
start = []
for _ in range(R):
    l = list(input().strip())
    g.append(l)
    if 'S' in l:
        start = [_, l.index('S')]

    for i, e in enumerate(l):
        if e == '*':
            q.append([_, i])
distance = [[0 for i in range(C)] for j in range(R)]
visited = [[0 for i in range(C)] for j in range(R)]
q.append(start)
dx, dy = [0, 1 ,0, -1], [1, 0, -1, 0]
while q:
    x, y = q.popleft()
    visited[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            continue

        if g[nx][ny] =='.' and g[x][y] == '*':
            q.append([nx, ny])
            g[nx][ny] = '*'
        elif g[nx][ny] == '.' and (g[x][y] == '.' or g[x][y] == 'S'):
            distance[nx][ny] = distance[x][y] + 1
            g[nx][ny] = 'S'
            q.append([nx, ny])
        elif g[nx][ny] == 'D' and (g[x][y] == '.' or g[x][y] == 'S'):
            print(distance[x][y] + 1)
            exit(0)

print("KAKTUS")



