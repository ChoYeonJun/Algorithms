from collections import deque

m, n = map(int, input().split())
g = []
idx = []
q = deque()

for i in range(n):
    l = list(map(int, input().split()))
    g.append(l)
    for j, e in enumerate(l):
        if e == 1:
            q.append([i, j])
def bfs():

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        a, b = q.popleft()

        v = g[a][b]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if g[nx][ny] == 0 :
                g[nx][ny] = (v + 1)
                q.append([nx, ny])

answer = 0
bfs()
for i in range(n):
    if 0 in g[i]:
        print(-1)
        exit(0)
    answer = max(answer, max(g[i]))
print(answer)