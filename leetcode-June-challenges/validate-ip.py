def validate_IPv4(ip: str) -> str:
    nums = ip.split('.')
    for num in nums:
        if len(num) == 0 or len(num) > 3:
            return 'Neither'
        if num[0] == '0' and len(num) != 1 or not num.isdigit() or int(num) > 255:
            return 'Neither'
    return 'IPv4'


def validate_IPv6(ip: str) -> str:
    nums = ip.split(':')
    hexdigits = '0123456789abcdefABCDEF'
    for num in nums:
        if len(num) == 0 or len(num) > 4 or not all(i in hexdigits for i in num):
            return 'Neither'
    return 'IPv6'


def validIPAddress(IP: str) -> str:
    if IP.count('.') == 3:
        return validate_IPv4(IP)
    elif IP.count(':') == 7:
        return validate_IPv6(IP)
    else:
        return 'Neither'


if __name__ == '__main__':
    print(validIPAddress('172.16.254.1'))
