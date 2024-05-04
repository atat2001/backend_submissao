user_input = input()


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

output = str(numberToBase(user_input,7)[0]) + str(numberToBase(200,7)[1]) + str(numberToBase(200,7)[2] )




print(output)