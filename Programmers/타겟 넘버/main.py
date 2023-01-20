from collections import deque

numbers = [4, 1, 2, 1]
target = 4

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])
    length = len(numbers)
    while q:
        value, idx = q.popleft()
        if idx+1 < length:
            q.append([value + numbers[idx + 1], idx + 1])
            q.append([value - numbers[idx + 1], idx + 1])
        else :
            if target == value:
                answer += 1


    return answer


print(solution(numbers, target))