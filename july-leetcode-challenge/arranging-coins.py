def arrangeCoins(n):
    if n == 1 or n == 0: return n
    sum = 0
    for i in range(1, n):
        sum += i
        if (n - sum) < (i + 1):
            return i


if __name__ == '__main__':
    print(arrangeCoins(8))
