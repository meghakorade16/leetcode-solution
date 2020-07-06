def main():
    s = ["h","e","l","l","o"]
    for i in range(0, len(s) // 2):
        s[i], s[-i - 1] = s[-i - 1], s[i]
    print(s)


if __name__ == '__main__':
    main()