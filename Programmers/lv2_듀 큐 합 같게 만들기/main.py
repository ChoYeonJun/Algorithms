def solution(queue1, queue2):
    answer = 0
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    target = (sum_q1 + sum_q2) // 2

    if (sum_q1 + sum_q2) % 2 != 0:  # 두 큐의 합계가 2로 안나눠 떨어지면 불가하다고
        return -1

    idx1 = 0
    idx2 = 0
    size_q1 = len(queue1)
    size_q2 = len(queue2)

    while sum_q1 != sum_q2:  # 두 큐의 합이 같을 때 까지
        if sum_q1 > sum_q2:
            if idx1 < size_q1:
                num = queue1[idx1]
            elif idx1 < size_q1 + size_q2: # queue1에 더 이상 순회할 값이 없다면 queue2 순회
                num = queue2[idx1 - size_q1]
            else:
                return -1  # 모든 값들을 순회했을 때 두 큐의 합이 같지 않으면 불가하다고 판단
            if num > target:
                return -1
            sum_q2 += num
            sum_q1 -= num
            idx1 += 1
        else:
            if idx2 < size_q2:
                num = queue2[idx2]
            elif idx2 < size_q2 + size_q1:  # queue2에 더 이상 순회할 값이 없다면 queue1 순회
                num = queue1[idx2 - size_q2]
            else:
                return -1  # 모든 값들을 순회했을 때 두 큐의 합이 같지 않으면 불가하다고 판단
            if num > target:  # 꺼낸 값이 target보다 크다면 불가하다고 판단
                return -1
            sum_q1 += num
            sum_q2 -= num
            idx2 += 1
        answer += 1
        if queue1 == [] or queue2 == []:
            return -1
    return answer