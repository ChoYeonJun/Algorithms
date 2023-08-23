def solution(k, ranges):
    points = [[0, k]]
    areas = []
    i = 0

    while k != 1:
        i += 1
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1

        points.append([i, k])
        be_point = points[-2]

        a = be_point[1]
        b = k
        area = (a + b) / 2

        if i != 1:
            area += areas[-1]

        areas.append(area)
    answer = []

    for r in ranges:
        a, b = r
        b += (len(points) - 1)

        if a > b:
            answer.append(float(-1))
            continue
        elif a == b:
            answer.append(float(0))
            continue

        area_a = 0
        if a != 0:
            area_a = areas[a - 1]

        area_b = areas[b - 1]
        answer.append(area_b - area_a)

    return answer