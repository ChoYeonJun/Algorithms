from collections import deque


def solution(order):
    answer = 0
    # box가 더 남아있지 않음을 나타내는 -1 추가
    boxes = [i + 1 for i in range(len(order))] + [-1]
    stack = []
    q = deque(boxes)
    idx = 0
    # 보조 컨테이너 벨트에서 박스 찾기
    def findBox(idx, answer):
        while stack:
            if stack[-1] == order[idx]:
                stack.pop(-1)
                idx += 1
                answer += 1
            else:
                return idx, answer

        return idx, answer

    while q:
        n = q.popleft()
        if n == order[idx]:
            idx += 1
            answer += 1
        else:
            v1, v2 = findBox(idx, answer)
            # 보조 컨테이너 벨트에 상자가 존재 하지 않고 q 마지막 값에 도달했을 때 return
            if v1 == idx and v2 == answer and n == -1:
                return answer
            idx, answer = v1, v2
            stack.append(n)

    return answer