import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
points = [int(input()) for _ in range(M)] + [L]


for _ in range(N):
    k = int(input())

    start = 1
    end = 4000000
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        left = 0
        cnt = 0
        for point in points:
            # 선택한 지점 이후 지점 간의 사이 값이
            # 지정한 mid 값 (임의 지정한 최소 길이)보다 크다면 cnt += 1
            # 또한 사이 값을 계산할 기준 값(left)을 조정한다.
            # 작다면 임의 지정한 최소 값의 존재 가치가 사라지므로,
            # 즉 mid 값이 최소 값이 아니게 되므로 기준 값을 재설정 하지 않고 넘어간다.
            if point - left >= mid:
                cnt += 1
                left = point
        # k개의 지점을 선택할 때 나오는 조각 수는 k + 1 개이다.

        # 각 지점간의 사이 값이 최소 값보다 큰 경우가 k 보다 많다면,
        # start 값을 조정하고 다시 수행한다.
        if cnt > k:
            answer = max(mid, answer)
            start = mid + 1
        else :
            end = mid - 1

    print(answer)