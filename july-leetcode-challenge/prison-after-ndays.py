def prisonAfterNDays(cells, N):
    N = (N - 1) % 14 + 1
    for _ in range(N):
        cells = nextDayState(cells)
    return cells


def nextDayState(cells):
    nex = [0] * len(cells)
    for i in range(1, len(cells) - 1):
        if cells[i - 1] == cells[i + 1]:
            nex[i] = 1
        else:
            nex[i] = 0
    return nex


if __name__ == '__main__':
    print(prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
