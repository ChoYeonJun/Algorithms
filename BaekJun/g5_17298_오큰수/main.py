n = int(input())
nums = list(map(int, input().split()))
stack = []
answer = [-1 for i in range(n)]
for i, n in enumerate(nums):
    while stack and stack[-1][1] < n:
        idx, v = stack.pop(-1)
        answer[idx] = n
    stack.append([i, n])

for a in answer:
    print(a, end=' ')
