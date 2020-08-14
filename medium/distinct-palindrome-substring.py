def function(string):
    ans = set()
    length = len(string)
    for center in range(2 * length - 1):
        left = int(center / 2)
        right = int(left + center % 2)
        while left >= 0 and right < length and string[left] == string[right]:
            ans.add(string[left: right + 1])
            left -= 1
            right += 1
    return ans


if __name__ == '__main__':
    print(function("abaaa"))
