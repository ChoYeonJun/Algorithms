def solution(dots):
    x1 = -1e9
    x2 = 1e9
    y1 = -1e9
    y2 = 1e9
    for dot in dots:
        x, y = dot
        x1 = max(x, x1)
        x2 = min(x, x2)

        y1 = max(y, y1)
        y2 = min(y, y2)

    return (x1 - x2) * (y1 - y2)