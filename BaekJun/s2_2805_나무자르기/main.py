n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)
answer = 0
# 36%
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in arr:
        if i > mid:
            result += (i - mid)
    if result >= m:
        answer = mid
        start = mid + 1
    elif result < m:
        end = mid - 1

print(answer)
