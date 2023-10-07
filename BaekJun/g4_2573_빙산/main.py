from collections import  deque
n, m = map(int, input().split())

graph = []
iced = []

for i in range(n):
    l = list(map(int, input().split()))
    for j, a in enumerate(l):
        if a != 0:
           iced.append([i, j])
    graph.append(l)

def process(r, c):
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    global iced
    q = deque([(r, c)])
    visited[r][c] = True

    on_process = {}
    while q:
        x, y = q.popleft()
        cnt = 0
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                cnt += 1
            elif graph[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True

        if cnt > 0:
            v = graph[x][y] - cnt
            if v < 0 :
                v = 0
            on_process[str(x) +',' + str(y)] = v
        else: on_process[str(x) +',' + str(y)] = graph[x][y]

    for a, b in iced:
        result = on_process.get(str(a)+','+str(b), -1)
        if result == -1:
            return True
        graph[a][b] = result
    iced = []

    for k in on_process.keys():
        if on_process[k] == 0:
            continue
        a, b = map(int, k.split(','))
        iced.append([a, b])
    return False

answer = 0

while True:
    visited = [[False for _ in range(m)] for __ in range(n)]
    result = False
    if iced:
        i = iced[0][0]
        j = iced[0][1]
        result = process(i, j)
        if result:
            print(answer)
            exit(0)
        answer += 1
    else:
        print(0)
        exit(0)

