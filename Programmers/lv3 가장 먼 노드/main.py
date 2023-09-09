import heapq

def solution(n, vertex):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append([b, 1])
        graph[b].append([a, 1])

    def dijkstra(start):
        q = []
        distance = [1e9 for _ in range(n + 1)]
        distance[start] = 0

        heapq.heappush(q, [0, start])
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] > dist:
                continue
            for to, cost in graph[now]:

                if distance[to] > cost + dist:
                    distance[to] = cost + dist
                    heapq.heappush(q, [cost + dist, to])

        return distance

    distance = dijkstra(1)
    cost = -1
    for d in distance:
        if d == 1e9:
            continue
        if d > cost:
            answer = 1
            cost = d
        elif d == cost:
            answer += 1
    return answer