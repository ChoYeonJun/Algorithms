from itertools import combinations


def solution(elements):
    totals = set()
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            subs = elements[j:i + j]
            if i + j > len(elements):
                end = i + j - len(elements) - 1
                subs += elements[: end]

            total = sum(subs)
            totals.add(total)

    return len(totals)