tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
# [['ICN', 'A'], ['A', 'B'], ['A', 'C'], ['C', 'A'], ['B', 'D']]
def solution(tickets):
    answer = []
    visited = [False for j in range(len(tickets))]

    def dfs(start, result):
        if False not in visited:
            answer.append(result)
            return

        for i, ticket in enumerate(tickets):
            if not visited[i] and start == ticket[0]:
                visited[i] = True
                dfs(ticket[1], result + [ticket[1]])
                visited[i] = False

    dfs('ICN', ['ICN'])

    return sorted(answer)[0]


print(solution(tickets))
