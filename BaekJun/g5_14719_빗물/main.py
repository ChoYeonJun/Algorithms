n, m = map(int, input().split())

heights = list(map(int, input().split()))
answer = 0
for i in range(n-1, -1, -1):
    cnt = -1
    for j, h in enumerate(heights):
        if h:
            if cnt != -1:
                answer += cnt
            cnt = 0
            heights[j] -= 1
        else :
            if cnt != -1:
                cnt += 1


print(answer)