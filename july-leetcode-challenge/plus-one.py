def plusOne(digits):
    x = len(digits) - 1
    while x >= 0:
        if digits[x] != 9:
            digits[x] += 1
            return digits
        digits[x] = 0
        x -= 1
    res = [] * (len(digits) + 1)
    res[0] = 1
    return res

    # num_string = ''
    # for i in digits:
    #     num_string += str(i)
    # number = int(num_string) + 1
    # digits = []
    # for i in range(len(str(number))):
    #     digits.append(int(str(number)[i]))
    # return digits


if __name__ == '__main__':
    print(plusOne([1, 2, 9]))
