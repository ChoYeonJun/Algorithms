# **문제**

길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 **다른 큐**에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.

큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다. 예를 들어 큐 `[1, 2, 3, 4]`가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 `[2, 3, 4]`가 되며, 이어서 5를 insert하면 `[2, 3, 4, 5]`가 됩니다.

다음은 두 큐를 나타내는 예시입니다.

`queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]`

두 큐에 담긴 모든 원소의 합은 30입니다. 따라서, 각 큐의 합을 15로 만들어야 합니다. 예를 들어, 다음과 같이 2가지 방법이 있습니다.

1. queue2의 4, 6, 5를 순서대로 추출하여 queue1에 추가한 뒤, queue1의 3, 2, 7, 2를 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [4, 6, 5], queue2는 [1, 3, 2, 7, 2]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 7번 수행합니다.
2. queue1에서 3을 추출하여 queue2에 추가합니다. 그리고 queue2에서 4를 추출하여 queue1에 추가합니다. 그 결과 queue1은 [2, 7, 2, 4], queue2는 [6, 5, 1, 3]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 2번만 수행하며, 이보다 적은 횟수로 목표를 달성할 수 없습니다.

따라서 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수는 2입니다.

길이가 같은 두 개의 큐를 나타내는 정수 배열 `queue1`, `queue2`가 매개변수로 주어집니다. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.

---

### 제한사항

- 1 ≤ `queue1`의 길이 = `queue2`의 길이 ≤ 300,000
- 1 ≤ `queue1`의 원소, `queue2`의 원소 ≤ 10
    
    9
    
- 주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.

---

### 입출력 예

| queue1 | queue2 | result |
| --- | --- | --- |
| [3, 2, 7, 2] | [4, 6, 5, 1] | 2 |
| [1, 2, 1, 2] | [1, 10, 1, 2] | 7 |
| [1, 1] | [1, 5] | -1 |

---

### 입출력 예 설명

**입출력 예 #1**

문제 예시와 같습니다.

**입출력 예 #2**

두 큐에 담긴 모든 원소의 합은 20입니다. 따라서, 각 큐의 합을 10으로 만들어야 합니다. queue2에서 1, 10을 순서대로 추출하여 queue1에 추가하고, queue1에서 1, 2, 1, 2와 1(queue2으로부터 받은 원소)을 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [10], queue2는 [1, 2, 1, 2, 1, 2, 1]가 되며, 각 큐의 원소 합은 10으로 같습니다. 이때 작업 횟수는 7회이며, 이보다 적은 횟수로 목표를 달성하는 방법은 없습니다. 따라서 7를 return 합니다.

**입출력 예 #3**

어떤 방법을 쓰더라도 각 큐의 원소 합을 같게 만들 수 없습니다. 따라서 -1을 return 합니다.

# 풀이

## 아이디어

- 합계가 큰 큐에 들어가 있는 수를 하나씩 다른 큐에 옮겨 가며 합계를 확인한다.

### 실패 코드

```python
from collections import deque
def solution(q1, q2):
    answer = 0
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    queue1 = deque(q1)
    queue2 = deque(q2)
    target = (sum_q1 + sum_q2) // 2

    if sum_q1 == sum_q2:
        return 0 # 두 큐의 합계가 같은 경우
    if (sum_q1 + sum_q2) % 2 != 0: # 두 큐의 합계가 2로 안나눠 떨어지면 불가하다고 
        return -1
    while sum_q1 != sum_q2: # 두 큐의 합이 같을 때 까지
        answer += 1
        if sum_q1 > sum_q2:
            num = queue1.popleft()
            if num > target:
                return -1
            queue2.append(num)
            sum_q2 += num
            sum_q1 -= num
        if sum_q2 > sum_q1:
            num = queue2.popleft()
            if num > target : # 꺼낸 값이 target보다 크다면 불가하다고 판단
                return -1
            queue1.append(num)
            sum_q1 += num
            sum_q2 -= num
        if queue1 == [] or queue2 == []:
            return -1
    return answer
```

- 시간 초과 발생
- [101, 100],[102, 103] 테스트 케이스를 돌려보면
    - 101, 100, 102 / 103
    - 100, 102 / 103, 101
    - 100, 102, 103/ 101
    - 102, 103 / 101, 100
- 다음과 같이 무한 루프가 발생함
- 처음 아이디어에서 합계가 큰 큐의 값을 하나씩 순회하는 방식인데,
- 모든 큐를 순회했을 경우 불가능 한 것으로 판단해야 한다
- 위 예에서는
    - 102
    - 101
    - 103
    - 100
- 순으로 반복 순회한다.
- 큐를 pop, append 하는 방식으로는 큐의 모든 원소를 순회했는지 확인하기 어려워 투포인터를 사용해 구현

### 성공 코드

```python
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
```