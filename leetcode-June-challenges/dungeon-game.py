def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
            elif i == m - 1:
                dungeon[i][j] = max(dungeon[i][j + 1] - dungeon[i][j], 1)
            elif j == n - 1:
                dungeon[i][j] = max(dungeon[i + 1][j] - dungeon[i][j], 1)
            else:
                dungeon[i][j] = max((min(dungeon[i][j + 1], dungeon[i + 1][j]) - dungeon[i][j]), 1)
        # print("\t" + str(i) + "\t" + str(j))
    return dungeon[0][0]


if __name__ == '__main__':
    # answer: 7
    print(calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
