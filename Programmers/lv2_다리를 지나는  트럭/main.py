from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 위에 있는 트럭들
    # 첫 트럭과 트럭의 위치를 초기값으로 가짐
    on_bridge = [[truck_weights[0], 0]]
    # 아직 다리에 올라가지 않은 트럭들
    q = deque(truck_weights[1:])
    # 다리 위에 있는 트럭 무게의 합
    # 첫 트럭으로 초기 값 설정
    cnt = truck_weights[0]

    # 모든 트럭이 지나가는데 필요한 시간
    # 첫 트럭이 올라가 있으므로 1초로 초기화
    answer = 1

    # 다리 위에 트럭이 있을 때
    while on_bridge:
        # 시간 소요
        answer += 1

        # 다리 위에서 내려간 트럭 지칭 인덱스
        idx = -1

        # 다리 위의 트럭 순회
        for i in range(len(on_bridge)):
            # 다리 위의 트럭 앞으로 위치 변경
            on_bridge[i][1] += 1

            # 트럭이 다리 위를 벗어났을 때
            if on_bridge[i][1] >= bridge_length:
                # 인덱스 변경
                idx = i
                # 다리 위의 트럭들 무게 빼기
                cnt -= on_bridge[i][0]

        # 지칭 인덱스가 변경됐고, 다리위에 트럭이 있을 때
        # 다리 위 트럭 정보 변경
        if idx != -1 and len(on_bridge) > idx:
            on_bridge = on_bridge[idx + 1:]

        # 출발하지 않은 트럭들이 있을 때
        # 다리가 트럭의 무게를 지탱할 수 있고, 들어갈 수 있는 거리가 있을 때
        if q and len(on_bridge) < bridge_length and cnt + q[0] <= weight:
            # 다리 위로 트럭 이동
            truck = q.popleft()
            on_bridge.append([truck, 0])
            cnt += truck

    return answer