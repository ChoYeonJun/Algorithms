def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = (i + 1) // n
        m = (i + 1) % n
        if m != 0:
            answer.append(max(v+1, m))
        else: answer.append(n)
    return answer
