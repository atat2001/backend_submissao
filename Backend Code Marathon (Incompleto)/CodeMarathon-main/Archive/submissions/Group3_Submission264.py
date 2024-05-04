user_input = input().split(',')

ana = user_input[0]
scooby = user_input[1]
atual = user_input[2]



if eval(ana [4:]) < eval(scooby [4:]):
    output = 'true'
    
elif eval(ana [4:]) > eval(scooby [4:]):
    output = ' false'
elif eval(ana[4:]) == eval(scooby [4:]):
    if eval(ana [2:4]) < eval(scooby [2:4]):
        output = 'true'
    elif eval(ana [2:4]) > eval(scooby [2:4]):
        output = 'false'
    elif eval(ana [2:4]) == eval(scooby [2:4]):
        if eval(ana [0:2]) < eval(scooby [0:2]):
            output = 'true'
        elif eval(ana [0:2]) >= eval(scooby [0:2]):
            output = 'false'



print(output)
