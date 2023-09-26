from itertools import product
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = []
virus = []
answer = 0
n_s = 0
for _ in range(n):
    l = list(map(int, input().split()))
    for i, e in enumerate(l):
        if e == 2:
            virus.append([_, i])
        elif e == 1:
            n_s += 1
    graph.append(l)

points = list(product([i for i in range(n)], [j for j in range(m)]))
combi = list(combinations(points, 3))

i, j, k = 0, 1, 2
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def bfs(s):
    q = deque(virus)
    cnt = len(virus) + n_s
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if s[nx][ny] == 0:
                s[nx][ny] = 2
                q.append([nx, ny])
                cnt += 1
    return cnt


for c in combi:
    x1, y1 = c[0]
    x2, y2 = c[1]
    x3, y3 = c[2]

    g = [item[:] for item in graph]

    if g[x1][y1] == 0:
        g[x1][y1] = 1
    if g[x2][y2] == 0:
        g[x2][y2] = 1
    if g[x3][y3] == 0:
        g[x3][y3] = 1
    answer = max(answer, n*m - bfs(g))
print(answer - 3)
