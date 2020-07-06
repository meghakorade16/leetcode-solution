def isSubsequence(s: str, t: str) -> bool:
    remainder_of_t = iter(t)
    for letter in s:
        if letter not in remainder_of_t:
            return False
    return True
    # t = iter(t)
    # return all(c in t for c in s)


if __name__ == '__main__':
    print(isSubsequence('', ''))
