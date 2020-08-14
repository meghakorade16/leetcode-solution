def removeComments(source):
    res, buff, isOpen = [], "", False
    for comment in source:
        n = len(comment)
        i = 0
        while i < n:
            if i - 1 < n and comment[i:i + 2] == "//" and not isOpen:
                break
            elif i - 1 < n and comment[i: i + 2] == "/*" and not isOpen:
                isOpen = True
                i += 1
            elif i-1<n and comment[i:i+2] == "*/" and isOpen:
                isOpen = False
                i += 1
            elif not isOpen:
                buff += comment[i]
            i += 1
        if buff and not isOpen:
            res.append(buff)
            buff = ""
    return res


if __name__ == '__main__':
    program = ["a/*comment", "line", "more_comment*/b"]
    result = removeComments(program)
    print(removeComments(program))
