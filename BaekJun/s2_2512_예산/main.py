n = int(input())

values = list(map(int, input().split()))
total = int(input())

if sum(values) <= total:
    print(max(values))
else :
    start = 0
    end = max(values)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for v in values:
            if v > mid:
                result += mid
            else: result += v
        if result > total:
            end = mid - 1
        elif result <= total:
            start = mid + 1
            answer = max(mid, answer)
    print(answer)

