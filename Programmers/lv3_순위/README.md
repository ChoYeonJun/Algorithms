# lv3 순위

# **문제**

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 선수의 수는 1명 이상 100명 이하입니다.
- 경기 결과는 1개 이상 4,500개 이하입니다.
- results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
- 모든 경기 결과에는 모순이 없습니다.

### 입출력 예

| n | results | return |
| --- | --- | --- |
| 5 | [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] | 2 |

### 입출력 예 설명

2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.

5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.

# 풀이

4는 3를 항상 이긴다, 3은 2를 항상 이긴다.

이 말은 4는 항상 2를 이긴다. 로 치환될 수 있다

그래프로 나타낼 수 있다.

4는 3으로 갈 수 있다, 3은 2로 갈 수 있다.

4는 2로 갈 수 있다.

각 노드가 연결되어 있는지 확인하면 된다.

→ [플로이드 워셜 알고리즘](https://www.notion.so/Floyd-Warshall-bcd2f904872244ac9f89c14716206ecc?pvs=21)을 사용한다.

```python
		answer = 0
    INF = 1e9
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
```

- 초기값을 세팅한다.
- 자기 자신 노드로 가는 것은 0으로 나타낸다.

```python
		for a, b in results:
        graph[a][b] = 1
    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
```

- 노드가 연결된 정보를 가진 results에서 값을 가져와 연결 됐음을 1로 표현한다.
- graph 내에서 한 노드가 다른 노드를 통해 최종 노드에 도달할 수 있는 지 확인한다.
- 초기 값은 1, INF, 0이므로 연결 됐음이 1이나 2로 표기될 것이다.

```python
		column_sum = [0]*(n + 1)
    row_sum = [0]*(n + 1)
    for row in range(n + 1):
        for column in range(n + 1):
            if graph[row][column] != INF and graph[row][column] != 0 :
                column_sum[column] += 1
                row_sum[row] += 1
		answer = 0
    for index in range(1, n + 1):
        print(column_sum[index] , row_sum[index])
        if column_sum[index] + row_sum[index] == n-1:
            answer+=1
```

- 입출력 예를 보면 “2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.” 라고 설명한다.
- 이는 한 승리할 수 있는 번호의 갯수와 지는 번호의 갯수의 합을 더했을 때 n - 1이 성립한다라는 것을 나타낸다.
- 즉, 한 노드에서 갈 수 있는 노드의 갯수와 노드로 올 수 있는 갯수의 합이 n - 1일 때 노드의 순위를 알 수 있다.

- graph에서 자기 자신 노드가 아니고(graph[row][col] 이 0이 아니고) INF가 아닌 값일 때 row 노드에서 column 노드로 갈 수 있음을 알 수 있다.
- 한 노드에서 갈 수 있는 노드의 갯수는 graph[x] 에서 INF, 0이 아닌 값의 갯수 `row_sum[x]` 이고
- 한 노드로 올 수 있는 노드의 갯수는 graph[1 ~ n][x]에서 INF, 0 이 아닌 값의 갯수 `column_sum[x]` 일 때
- `row_sum[x] + column_sum[x] == n-1` 이 성립하면 임의의 번호 x의 순위를 알 수 있다.