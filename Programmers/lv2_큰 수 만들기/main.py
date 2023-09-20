def solution(number, k):
    answer = ''
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)