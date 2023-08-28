def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []
    for i, number in enumerate(numbers):
        while stack and stack[-1][1] < number:
            idx = stack[-1][0]
            stack.pop()
            answer[idx] = number
        stack.append([i, number])

    return answer