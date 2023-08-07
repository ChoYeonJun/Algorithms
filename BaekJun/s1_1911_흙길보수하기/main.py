n, l = map(int,input().split())

answer = 0
points = []
for i in range(n):
    a, b = map(int,input().split())
    points.append([a, b])

points = sorted(points,key=lambda a: a )
j = 1
end_l = 0

for i in range(len(points)):
    a, b = points[i]
    j = 1
    if end_l > b:
        continue
    if a <= end_l:
        a = end_l

    j = (b - a) // l
    if (b - a) % l != 0:
        j += 1
    answer += j

    end_l = a + j * l



print(answer)