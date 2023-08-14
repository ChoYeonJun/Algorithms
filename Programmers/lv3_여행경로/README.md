# lv3 여행경로

### **문제 설명**

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

### 입출력 예

| tickets | return |
| --- | --- |
| [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] | ["ICN", "JFK", "HND", "IAD"] |
| [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] | ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] |

### 입출력 예 설명

예제 #1

["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2

["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

## 풀이

## 테스트 케이스 1번 실패

```java
def solution(tickets):
    answer = []

    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            visited = [False for j in range(len(tickets))]
            sub_ans = dfs(i, tickets, visited, ["ICN"])
            if not False in visited:
                answer.append(sub_ans)
    return sorted(answer, key = lambda x : x)[0]

def dfs(idx, tickets, visited, answer):
    start, end = tickets[idx]
    answer.append(end)
    
    visited[idx] = True
    for i, ticket in enumerate(tickets):
        if not visited[i] and ticket[0] == end:
            dfs(i, tickets, visited, answer)
    if False not in visited:
        return answer
```

- 방향은 맞았으나 로직 구현이 꼬이고 꼬여서 테스트 케이스 1번을 못 푼 문제
- 우선 1번이 틀린 이유로 나온 반례는 다음과 같다
    
    `[['ICN', 'A'], ['A', 'B'], ['A', 'C'], ['C', 'A'], ['B', 'D']]`
    
    ICN → A → B → D에서 멈추고 
    
    ICN → A → C → A …로 진행되어야 하는데
    
    멈춘 후 돌아갔을 때의 상태를 보존하고 있지 못했다. 
    
    즉, visited와 answer가 중간 로직에 영향을 계속 받아 값이 변경됐다.
    
- 때문에 deepcopy를 통해 매번 새 변수로 복제하려고 했다.

```java
import copy
final = []
def solution(tickets):
    answer = []

    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            visited = [False for j in range(len(tickets))]
            dfs(i, tickets, visited, ["ICN"])

    return sorted(final, key=lambda x: x[1])[0]

def dfs(idx, tickets, visited, answer):

    result = copy.deepcopy(answer)
    result.append(tickets[idx][1])

    isVisited = copy.deepcopy(visited)
    isVisited[idx] = True
    if False not in isVisited:
        global final
        final.append(result)

    for i, ticket in enumerate(tickets):
        if not isVisited[i] and ticket[0] == result[-1]:
            dfs(i, tickets, isVisited, result)
```

- copy를 통해 로직 도중 원하는 값을 result에 담아낼 수 있었지만 1번 테스트 케이스에서 여전히 오류가 발생했다.

### 정답 코드

```java
def solution(tickets):
    answer = []
    visited = [False for j in range(len(tickets))]

    def dfs(start, result):
        if False not in visited:
            answer.append(result)
            return

        for i, ticket in enumerate(tickets):
            if not visited[i] and start == ticket[0]:
                visited[i] = True
                dfs(ticket[1], result + [ticket[1]])
                visited[i] = False

    dfs('ICN', ['ICN'])

    return sorted(answer)[0]
```

- https://lottegiantsv3.tistory.com/27 를 참조했다.
- 파이썬은 메소드 안에 메소드 선언이 가능하기 때문에 굳이 위 코드의 final처럼 전역변수를 선언하지 않아도 된다.
- 또한 dfs이후 visit의 값을 방문하지 않음으로 돌려놓음으로써 중간 로직이 결과 값에 영향을 주지 못하게 한다.
- 프로그래머스 문제는 메서드를 solution 안에 넣는 것을 계속 고려해야 겠다.