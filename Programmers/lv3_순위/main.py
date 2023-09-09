def solution(n, results):
    answer = 0
    INF = 1e9
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    for a, b in results:
        graph[a][b] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    column_sum = [0] * (n + 1)
    row_sum = [0] * (n + 1)
    for row in range(n + 1):
        for column in range(n + 1):
            if graph[row][column] != INF and graph[row][column] != 0:
                column_sum[column] += 1
                row_sum[row] += 1

    answer = 0
    for index in range(1, n + 1):
        print(column_sum[index], row_sum[index])
        if column_sum[index] + row_sum[index] == n - 1:
            answer += 1

    return answer