import string
user_input = int(input())


# def numberToBase(n, b):
#     if n == 0:
#         return [0]
#     digits = []
#     while n:
#         digits.append(int(n % b))
#         n //= b
#     return digits[::-1]

# output = numberToBase(user_input,7).join()


digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

output = int2base(user_input, 7)



print(output)