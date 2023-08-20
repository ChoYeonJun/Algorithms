import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        # node 중 최단 거리를 가진 node를 pop
        distance_now, now = heapq.heappop(q)
        
        # 이미 방문한 노드면 pass
        # 최단 거리를 가진 순으로 노드를 pop하기 때문에 이전에 값이 설정 됐다면 
        # 방문한 노드이다.
        if distance_now > distance[now]:
            continue
        
        # 현재 node now와 연결된 node를 순회 
        for info in graph[now]:
            to, distance_to = info
            # 현재 node 와 연결된 node 중 distance 값이
            # 이전 노드에서부터 직접 연결 되어 방문한 값보다 작거나
            # 혹은 아직 방문하지 않은 값이라면 거리 값을 담은 table를 갱신한다.
            # 또한 우선순위 q에 push 한다
            if distance_now + distance_to < distance[to]:
                cost = distance_now + distance_to
                distance[to] = cost
                heapq.heappush(q, [cost, to])
    print(distance)
#input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 4 2
# 2 3 3
# 3 2 3
# 3 6 5
# 4 5 1
# 4 3 3
# 5 3 1
# 5 6 2

# output 
# [1000000000, 0, 2, 3, 1, 2, 4]

print(dijkstra(1))