def solution(k, score):
    answer = []
    l = []
    for num in score:
        l = sorted(l)
        if len(l) >= k:
            l[0] = max(num, l[0])
        else:
            l.append(num)
        answer.append(min(l))

    return answer