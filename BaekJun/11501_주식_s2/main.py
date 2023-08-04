
n = int(input())

# 테스트 케이스 수 만큼 반복
for i in range(n):
    t = int(input())
    answer = 0

    l = list(map(int, input().split()))
    # 최대 값의 인덱스를 찾기 위한 딕셔너리 선언
    # key - list value, value - list index
    # 딕셔너리 value들은 늦게 나온 인덱스가 최종값이 된다.
    dict_l = {k: v for v, k in enumerate(l)}

    # 최고가에서 뺄 주가 값 인덱스 시작점
    idx_front = 0

    # 시작점이 리스트 길이보다 커질 때 까지 실행
    while idx_front < len(l):

        # 시작 점부터 제일 큰 값 찾기
        big = max(l[idx_front:])
        # 최고가의 제일 마지막 인덱스 가져오기
        idx_big = dict_l[big]

        # 큰 값의 인덱스가 시작점보다 작으면 넘어가도록
        if idx_front > idx_big :
            # idx_front = idx_big + 1
            continue

        # 시작 점부터 큰 값의 인덱스까지 반복
        for j in range(idx_front, idx_big):
            # 정답에 최고가 - 주가 더하기
            answer += (big - l[j])

        # 시작점을 최고가 인덱스 + 1 로 설정
        idx_front = idx_big + 1

    print(answer)


