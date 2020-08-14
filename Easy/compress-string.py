def compress(chars):
    i, result = 0, ""
    while i < len(chars):
        char, length = chars[i], 1
        while (i + 1) < len(chars) and char == chars[i + 1]:
            length, i = length + 1, i + 1
        if length > 1:
            result = result + char + str(length)
        i += 1
    return result


if __name__ == '__main__':
    print(compress("aabbccc"))
