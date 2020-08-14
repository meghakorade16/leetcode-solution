def order_tracker(heights):
    height_feq = [0] * 101
    for i in heights:
        height_feq[i] += 1
    result, correct_height = 0, 0
    for i in range(len(heights)):
        while height_feq[correct_height] == 0:
            correct_height += 1
        if heights[i] != correct_height:
            result += 1
        height_feq[correct_height] -= 1
    return result


if __name__ == '__main__':
    print(order_tracker([1, 1, 4, 2, 1, 3]))
