import functools
citations = [2,2,2,2,2] #h=3
            # 6 2 2 1 0
            # 1 2 4 5 6
            # 1 1 1 1 0

def solution(citations):
    citations.sort(reverse=True)
    subs = 1e9
    answer = 0
    for i in range(len(citations)):
        if subs > abs(citations[i] - i):
            answer = min(i+1, citations[i])
            subs =  abs(citations[i] - i)

    return answer
print(solution(citations))