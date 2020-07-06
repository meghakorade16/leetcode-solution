def main():
    costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
    min_cost = 0
    diff = {}
    for element in costs:
        min_cost += element[0]
        diff.update({costs.index(element): element[0] - element[1]})
    sorted_diff = {k: v for k, v in sorted(diff.items(), key=lambda item: item[1], reverse=True)}
    for i in range(int(len(costs) / 2)):
        min_cost -= costs[list(sorted_diff)[i]][0]
        min_cost += costs[list(sorted_diff)[i]][1]
    print(min_cost)


if __name__ == '__main__':
    main()
