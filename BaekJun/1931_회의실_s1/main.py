from collections import defaultdict

n = int(input())
# 입력
time_table = []
for i in range(n):
    a, b = map(int, input().split())

# 종료 시간과 시작 시간을 각각 첫번째 두번째 기준으로 정렬
time_table = sorted(time_table, key=lambda x : (x[1], x[0]))
cnt = 0
now = 0
# 정렬 된 리스트에서 이전 회의 종료 시간과 현재 회의 시작 시간 비교하여 카운트
for i, [a, b] in enumerate(time_table, start=1):
    if a < now:
        continue
    cnt += 1
    now = b
print(cnt)

