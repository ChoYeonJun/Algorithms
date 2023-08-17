rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]

def draw_map(rectangle):
    graph = [[0 for i in range(51)]] * 51
    for r in rectangle:
        lx, ly, hx, hy = r[0], r[1], r[2], r[3]
        for i in range(hx - lx):



print(draw_map(rectangle))