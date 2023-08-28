import heapq
def solution(operations):
    q = []
    minus_q = []
    for op in operations:
        if op == "D 1" :
            if q and minus_q:
                n = heapq.heappop(minus_q)
                q.remove(-1 * n)
        elif op == "D -1" :
            if minus_q and q:
                n = heapq.heappop(q)
                minus_q.remove(-1 * n)
        else :
            num = int(op.split()[1])
            heapq.heappush(q, num)
            heapq.heappush(minus_q, -1 * num)
        # print(q)
        # print(minus_q)
    if q :
        return [-1 * heapq.heappop(minus_q), heapq.heappop(q)]
    else : return [0, 0]
