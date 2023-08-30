k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for line in lines:
        total += (line // mid)

    if total >= n:
        start = mid + 1
        answer = max(answer, mid)
    else :
        end = mid - 1
print(answer)