def reverseWords(s: str):
    # word = s.split(" ")
    # result = ''
    # for i in reversed(word):
    #     if i == '':
    #         continue
    #     result += i + ' '
    # print(result[:-1])
    return " ".join(s.split()[::-1])


if __name__ == '__main__':
    print(reverseWords("a good   example"))
