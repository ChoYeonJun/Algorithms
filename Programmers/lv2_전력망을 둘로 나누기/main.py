
import copy
from collections import deque


def solution(n, wires):
    answer = 1e9
    for i in range(len(wires)):
        graph = copy.deepcopy(wires)
        graph.pop(i)
        # print(graph)
        visited = [False for i in range(n + 1)]

        q = deque([graph[0][0]])
        l = [graph[0][0]]
        while q:
            # size += 1
            start = q.popleft()
            visited[start] = True

            for wire in graph:
                if wire[0] == start and not visited[wire[1]] and wire[1] not in l :
                    q.append(wire[1])
                    l.append(wire[1])
                elif wire[1] == start and not visited[wire[0]] and wire[0] not in l:
                    q.append(wire[0])
                    l.append(wire[0])

        size = len(l)
        answer = min(answer, abs(-n + size*2))

    return answer

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))