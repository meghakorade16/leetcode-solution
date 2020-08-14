def decode(s):
    substring = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            substring.append(s[i])
        elif s[i] == ')':
            temp = ''
            while substring[len(substring) - 1] != '(':
                temp = substring.pop() + temp
            substring.pop()
            substring.append(temp)
        elif s[i] == '{':
            i += 1
            num = ''
            while i < len(s) and s[i] != '}':
                num += s[i]
                i += 1
            pre = substring.pop()
            substring.append(pre * int(num))
        else:
            substring.append(s[i])
        i += 1
    return ''.join(substring)


if __name__ == '__main__':
    print(decode("(ab(d){3}){2}"))
