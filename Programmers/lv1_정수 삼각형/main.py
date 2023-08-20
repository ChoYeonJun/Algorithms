import copy

def solution(triangle):
    dp = copy.deepcopy(triangle)
    dp[0] = ([triangle[0][0]])

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = (dp[i - 1][0] + triangle[i][0])
            elif j == len(triangle[i]) - 1:
                dp[i][j] = (dp[i - 1][j - 1] + triangle[i][j])
            else:
                dp[i][j] = (max(dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j]))
    return max(dp[len(triangle) - 1])
