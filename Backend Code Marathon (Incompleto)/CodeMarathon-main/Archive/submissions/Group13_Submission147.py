

if __name__ == '__main__':
    j = 0
    liner = str(input(""))
    res = 0
    line = [int(it) for it in liner] 
    
    for i in range(len(line)):
        if line[i] == 0 or i < j:
            continue
        tmp = 0
        for j in range(i + 1, len(line)):
            if line[j] < line[i]:
                tmp += line[i] - line[j]
            elif line[j] >= line[i]:
                res += tmp
                break
            if j == len(line) - 1:
                j = i
    
    print(res) 
        
                
    