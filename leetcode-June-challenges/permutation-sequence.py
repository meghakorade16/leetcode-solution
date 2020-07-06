def getPermutation(n, k):
    numbers = list(range(1, n + 1))
    answer = ''

    for _ in range(n):
        d = (k - 1) // factorial(n - 1)
        k -= d * factorial(n - 1)
        n -= 1
        answer += str(numbers[d])
        numbers.remove(numbers[d])

    return answer


def factorial(number):
    factorial = 1
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        for i in range(1, number + 1):
            factorial *= i
        return factorial


if __name__ == '__main__':
    print(getPermutation(6, 314))
