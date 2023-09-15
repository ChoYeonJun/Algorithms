def solution(board, skill):
    answer = 0
    cal = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]  # 누적합 기록을 위한 배열

    # 누적합 계산을 위한 리스트 초기화
    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            degree -= degree * 2
        cal[r1][c1] += degree
        cal[r2 + 1][c1] -= degree
        cal[r1][c2 + 1] -= degree
        cal[r2 + 1][c2 + 1] += degree

    # 같은 행에 대한 누적합 계산
    for i in range(len(board)):
        for j in range(len(board[0])):
            cal[i][j + 1] += cal[i][j]
    # 같은 열에 대한 누적합 계산
    for i in range(len(board[0])):
        for j in range(len(board)):
            cal[j + 1][i] += cal[j][i]
    # 누적합 건물 리스트에 적용
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += cal[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer