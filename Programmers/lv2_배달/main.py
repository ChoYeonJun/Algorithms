import heapq

n = 5
arr = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]


def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N + 1)]
    for info in road:
        fm, to, dist = info
        graph[fm].append([to, dist])
        graph[to].append([fm, dist])
    distance = dijkstra(1, N + 1, graph)
    for i in range(1, len(distance)):
        if distance[i] <= K:
            answer += 1
    return answer


def dijkstra(start, n, graph):
    q = []
    heapq.heappush(q, (0, start))
    distance = [int(1e9) for i in range(n + 1)]
    distance[start] = 0
    while q:
        distance_now, now = heapq.heappop(q)
        if distance_now > distance[now]:
            continue

        for info in graph[now]:
            to, distance_to = info
            cost = distance_now + distance_to
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(q, (cost, to))

    return distance


solution(n, arr, 3)
