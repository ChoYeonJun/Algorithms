def solution(park, routes):
    dict_dir = {'E': [0, 1], 'S': [1, 0], 'W': [0, -1], 'N': [-1, 0]}

    start = [-1, -1]
    for i, point in enumerate(park):
        for j, p in enumerate(point):
            if p == 'S':
                start = [i, j]
    x, y = start

    for route in routes:
        key, cnt = route.split()
        dx, dy = dict_dir[key]

        dx *= int(cnt)
        dy *= int(cnt)

        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
            continue

        dx, dy = dict_dir[key]
        for i in range(1, int(cnt) + 1):
            nx = x + dx * i
            ny = y + dy * i
            if park[nx][ny] == 'X':
                break
        if park[nx][ny] == 'X':
            continue
        x, y = nx, ny
    return [x, y]