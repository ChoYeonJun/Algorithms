from collections import Counter


def solution(n):
    cnt = Counter(bin(n))['1']
    cpr = n + 1
    while Counter(bin(cpr))['1'] != cnt:
        cpr += 1

    return cpr