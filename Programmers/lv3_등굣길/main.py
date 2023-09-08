def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]

    for i in range(1, m + 1):
        dp[1][i] = 1

    for i in range(1, n + 1):
        dp[i][1] = 1

    for a, b in puddles:
        dp[b][a] = -1
        if a == 1:
            for i in range(b + 1, n + 1):
                dp[i][1] = -1
        elif b == 1:
            for i in range(a + 1, m + 1):
                dp[1][i] = -1

    for x in range(2, n + 1):
        for y in range(2, m + 1):

            if dp[x][y] == -1:
                continue
            if dp[x][y - 1] != -1:
                dp[x][y] += dp[x][y - 1]
            if dp[x - 1][y] != -1:
                dp[x][y] += dp[x - 1][y]

            dp[x][y] %= (1e9 + 7)
    print(dp)

    return int(dp[n][m])