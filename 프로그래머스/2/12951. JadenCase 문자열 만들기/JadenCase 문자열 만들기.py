def solution(s):
    answer = ''
    string = list(map(str,s.split()))
    blank =  list(map(str,s.split()))
    
    for i in range(len(string)):
        l = list(string[i])
        
        for j in range(len(string[i])):
            if string[i][j].isupper():
                l[j] = l[j].lower()

        if l[0].isalpha():
            l[0] = l[0].upper()
            
        
        answer += "".join(l)
    answer = list(answer)        
    re = -1
    for i in range(s.count(' ')):
        re = s.index(' ', re + 1)
        answer.insert(re," ")
    
    return "".join(answer)