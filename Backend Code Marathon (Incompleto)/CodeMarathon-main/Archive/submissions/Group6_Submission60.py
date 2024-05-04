

digits = eval(input())
if digits[0] == 0: raise ValueError
possible_digit1 = (digits[0] - 1) * digits[1]
possible_digit2 = (digits[0] - 1) * digits[2]
if digits[0] == 1: print(1)
else:
    if possible_digit1 % digits[1] == 0 and possible_digit1 % digits[2] != 0:
        print(possible_digit1)
    else:
        print(possible_digit2)

