computers = [[1, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 1, 1],
 [1, 0, 1, 1, 1, 1],
 [1, 0, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1]]

def solution(n, computers):
    answer = 0
    graph = []
    visited = [False] * n

    for i, c in enumerate(computers):
        sub_g = []
        for j in range(len(c)):
            if i != j and c[j] == 1:
                sub_g.append(j)
        graph.append(sub_g)
    for k in range(n):
        if not visited[k] and dfs(graph, k, visited):
            answer += 1

    return answer


def dfs(graph, v, visited):
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    if len(graph[v]) == 0:
        return True

    if not visited[v]:
        # 현재 노드를 방문 처리
        visited[v] = True
        # 현재 노드와 연결된 모든 노드에 대해 방문 처리
        for i in graph[v]:
            dfs(graph, i, visited)
        return True
    return False

print(solution(6, computers))


