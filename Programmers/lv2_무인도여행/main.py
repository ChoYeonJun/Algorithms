import sys

def solution(maps):
    limit_number = 10000
    sys.setrecursionlimit(limit_number)
    answer = []

    def dfs(x, y):
        if x >= len(maps) or x < 0 or y >= len(maps[0]) or y < 0:
            return 0
        if maps[x][y] != 'X':
            value = int(maps[x][y])

            s = list(maps[x])
            s[y] = 'X'
            maps[x] = "".join(s)

            value += dfs(x + 1, y)
            value += dfs(x - 1, y)
            value += dfs(x, y + 1)
            value += dfs(x, y - 1)

            return value
        return 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                result = dfs(i, j)
                if result != 0:
                    answer.append(result)

    if len(answer) != 0:
        return sorted(answer)

    return [-1]