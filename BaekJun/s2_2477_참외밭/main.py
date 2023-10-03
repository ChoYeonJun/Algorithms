k = int(input())

info = []
for i in range(6):
    info.append(list(map(int, input().split()))[1])

big = 0
point = 0
for i, data in enumerate(info):
    size = data
    if size > big:
        big = size
        point = i


sort_info = info[point:] + info[:point]

result = sort_info[1] * sort_info[2] + sort_info[-1]*sort_info[-2]

print(result * k)

