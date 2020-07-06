def Add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


if __name__ == '__main__':
    print(Add(4, 2))