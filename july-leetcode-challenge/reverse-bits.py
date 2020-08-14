def reverse(n: int) -> int:
    rev = 0
    for i in range(32):
        rev = (rev << 1) ^ (n & 1)
        n >>= 1
    return rev


if __name__ == '__main__':
    print(reverse(2))
