def nthUglyNumber(n: int):
    if n <= 0:
        return 0
    ugly = [1]
    twoIndex, threeIndex, fiveIndex = 0, 0, 0
    while len(ugly) < n:
        by2 = ugly[twoIndex] * 2
        by3 = ugly[threeIndex] * 3
        by5 = ugly[fiveIndex] * 5
        mini = min(by2, min(by3, by5))
        ugly.append(mini)
        if mini == by2:
            twoIndex += 1
        if mini == by3:
            threeIndex += 1
        if mini == by5:
            fiveIndex += 1
    return ugly[n - 1]


if __name__ == '__main__':
    print(nthUglyNumber(10))
