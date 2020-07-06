def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in coins:
        for j in range(i, amount + 1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[amount]


if __name__ == '__main__':
    list = [1, 2, 5]
    count = change(5, [1, 2, 5])
    print(count)
