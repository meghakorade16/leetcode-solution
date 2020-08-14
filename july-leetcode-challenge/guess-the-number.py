def getMoneyAmount(n):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n, 0, -1):
        print("i: ", i)
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 0
            if j - i == 1:
                dp[i][j] = i
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], max(dp[i][k - 1] + k, dp[k + 1][j] + k))
    print(dp)


if __name__ == '__main__':
    getMoneyAmount(3)
