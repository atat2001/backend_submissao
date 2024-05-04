numbers = ["0","1","2","3","4","5","6","7","8","9"]


if __name__ == '__main__':
    liner = input("")
    line = liner.split(",")
    res = ""
    for i in range(len(line[0])):
        char = line[0][i] 
        if char not in numbers:
            res += char
            continue
        else:
            tmp = ""
            for j in line[0][i:]:
                if j in numbers:
                    tmp += j
                else:
                    break            
            for _ in range(int(tmp) - 1):
                res += res                
    print(res[int(line[1]) - 1])
    
    
    
 