def vindimas(input):
    input = str(input)
    counter = 0
    res = 0
    for i in input:
        i = int(i)
        if i != 0:
            if int(input[counter+1]) == 0:
                if int(input[counter + 2]) != 0:
                    res += min(i,input[counter+2])
            elif int(input[counter+1]) < i:
                res += i-int(input[counter+1])
    return res