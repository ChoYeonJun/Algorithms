from collections import Counter
def solution(topping):
    answer = 0
    a = set()
    b = Counter(topping)

    for t in topping:
        b[t] -= 1
        if b[t] == 0:
            b.pop(t)
        a.add(t)

        if len(a) == len(b.keys()):
            answer += 1
        if len(a) > len(b.keys()):
            break
    return answer
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))