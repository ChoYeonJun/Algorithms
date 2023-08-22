def solution(n, times):
    start = min(times)
    end = max(times) * n
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for time in times:
            result += (mid // time)
        if result >= n:
            answer = mid
            end = mid - 1
        elif result < n:
            start = mid + 1

    return answer

n = 6
times = [1, 1, 1, 1000]

print(solution(n, times))