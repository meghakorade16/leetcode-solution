def addBinary(a: str, b: str) -> str:
    result = ''
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    while i >= 0 or j >= 0:
        addition = carry
        if i >= 0:
            addition += int(a[i])
        if j >= 0:
            addition += int(b[j])
        result += str(addition % 2)
        carry = addition / 2
        i -= 1
        j -= 1
    if carry != 0:
        result += str(carry)
    return result


if __name__ == '__main__':
    print(addBinary('11', '1'))
