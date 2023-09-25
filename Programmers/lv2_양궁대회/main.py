from itertools import product

def solution(n, info):
    info.reverse()
    answer = [-1]
    # 11개의 인덱스에서 더 많이 쐈고 못 쐈고를 나타내는 경우의 수 리스트 순회
    # FFFFFFFFFF
    # FFFFFFFFF T
    # FFFFFFFF T F
    # ...
    result = 0
    for wl in product((True, False), repeat=11):
        # True인 경우 어피치보다 1발 더 쐈다고 가정 후 총 몇발 쐈는지 계산
        total = sum(info[i] + 1 for i in range(11) if wl[i])

        # 쏜 화살의 갯수가 n 발 이하일 때
        if total <= n:
            # 라이언, 어피치 점수 계산
            apeach = sum(i for i in range(11) if not wl[i] and info[i])
            ryan = sum(i for i in range(11) if wl[i])
            subs = ryan - apeach

            # 점수 차가 더 클 때
            if subs > result:
                result = subs
                # apeach 보다 한발 더 쐈을 때, 안 쐈을 때
                answer = [info[i] + 1 if wl[i] else 0 for i in range(11)]
                # 마지막에 남은 화살 0점에 버리기
                # for 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
                answer[0] += n - total
    answer.reverse()
    return answer