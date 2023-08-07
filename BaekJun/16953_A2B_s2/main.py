a, b = map(int, input().split())

cnt = 1
while a < b:

    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
        cnt += 1
        continue

    if b % 2 == 0:
        b //= 2
        cnt += 1
        continue

    break

if a != b:
    print(-1)
else:
    print(cnt)

