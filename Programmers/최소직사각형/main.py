sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    x = 0
    y = 0
    for size in sizes:

        a, b = size
        big = max(a, b)
        small = min(a, b)

        x = max(x, big)
        y = max(y, small)

    return x*y

print(solution(sizes))