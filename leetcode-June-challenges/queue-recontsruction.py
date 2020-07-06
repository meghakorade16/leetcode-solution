def main():
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    d = {}
    for h, k in people:
        if h not in d:
            d[h] = [[h, k]]
        else:
            d[h].append([h, k])
    re = []
    for h in sorted(d.keys(), reverse=True):
        group = sorted(d[h])
        if not re:
            re += group
        else:
            for h, k in group:
                re.insert(k, [h, k])
    print(re)


if __name__ == '__main__':
    main()
