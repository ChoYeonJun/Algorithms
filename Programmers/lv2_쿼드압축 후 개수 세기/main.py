def solution(arr):
    answer = [0, 0]

    def getsubgrid(x1, y1, n, grid):
        sub = []
        for item in grid[y1:y1 + n]:
            sub.append(item[x1:x1+n])
        return sub

    def compress(n, grid):
        if n == 1:
            answer[grid[0][0]] += 1
        else:
            size = n // 2
            start = grid[0][0]
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] != start:
                        compress(size, getsubgrid(0, 0, size, grid))
                        compress(size, getsubgrid(size, 0, size, grid))
                        compress(size, getsubgrid(0, size, size, grid))
                        compress(size, getsubgrid(size, size, size, grid))
                        return
            answer[grid[0][0]] += 1
    compress(len(arr), arr)
    return answer


arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))