def solution(num, total):
    for i in range(1000, -50, -1):
        l = []
        for j in range(num):
            l.append(i - j)
        if sum(l) == total:
            return sorted(l)
