targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
from collections import defaultdict
from collections import deque
def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x : x[1] - x[0])
    # sort_targets = sorted(targets, key=lambda x : x[0])
    isVisited = [False for i in range(len(targets))]
    target_dict = {}
    for v, k in enumerate(targets):
        target_dict[tuple(k)] = v

    for i in range(len(targets)):
        s, e = targets[i]
        if isVisited[target_dict[s, e]]:
            continue
        isVisited[target_dict[s, e]] = True
        for j in range(i, len(targets)):
            a, b = targets[j]
            if isVisited[target_dict[a, b]]:
                continue
            if a == s and b == e : continue
            if (s <= a < e <= b) or (a <= s < b <= e) or (s >= a and b >= e):
                    idx = target_dict[a, b]
                    isVisited[idx] = True


        answer += 1

    return answer


print(solution(targets))