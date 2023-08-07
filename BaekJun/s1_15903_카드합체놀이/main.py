n, m = map(int, input().split())

l = list(map(int, input().split()))

for i in range(m):
    l = sorted(l)
    a, b = l[0], l[1]
    l[0] = a+b
    l[1] = a+b
print(sum(l))
