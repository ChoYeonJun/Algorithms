def solution1(rows, columns, queries):
    answer = []
    graph = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]

    def rotate(x1, y1, x2, y2):

        len_x = x2 - x1  # 3
        len_y = y2 - y1  # 2
        grid = [[1e9 for i in range(len_y + 1)] for j in range(len_x + 1)]
        # for i in range(x1, x2):
        for i in range(1, len_x + 1):
            grid[i - 1][0] = graph[x1 + i - 1][y1 - 1]
            grid[len_x - i + 1][len_y] = graph[x2 - i - 1][y2 - 1]

        for j in range(1, len_y + 1):
            grid[0][j] = graph[x1 - 1][y1 + j - 2]
            grid[len_x][len_y - j] = graph[x2 - 1][y2 - j]

        result = 1e9
        for i, row in enumerate(grid):
            result = min(result, min(row))
            for j in range(len(grid[0])):
                if grid[i][j] != 1e9:
                    graph[x1 + i - 1][y1 + j - 1] = grid[i][j]
        # print(graph)
        return result

    for query in queries:
        x1, y1, x2, y2 = query
        answer.append(rotate(x1, y1, x2, y2))
    # rotate(2,2,5,4)
    return answer


# 스택을 이용한 풀이
def solution(rows, columns, queries):
    answer = []
    # 초기 그래프 생성
    graph = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        stack = []

        # y2 열에 해당하는 좌표 값 순회
        for i in range(x1, x2 + 1):
            # stack에 좌표값 append
            stack.append(graph[i][y2])

            # 1개의 값만 있을 때는 넘어가도록
            if len(stack) == 1:
                continue
            else:
                # 스택에 넣었던 값으로 변경, 그래프 회전 적용
                graph[i][y2] = stack[-2]
        # x2 행에 해당하는 좌표 값 순회
        for i in range(y2 - 1, y1 - 1, -1):
            stack.append(graph[x2][i])
            graph[x2][i] = stack[-2]

        # y1 열에 해당하는 좌표 값 순회
        for i in range(x2 - 1, x1 - 1, -1):
            stack.append(graph[i][y1])
            graph[i][y1] = stack[-2]

        # x1 행에 해당하는 좌표 값 순회
        for i in range(y1 + 1, y2 + 1):
            stack.append(graph[x1][i])
            graph[x1][i] = stack[-2]

        # 스택 값중 최소 값 찾기
        answer.append(min(stack))

    return answer
solution(6, 6, [[2,2,5,4]])