def solution(s):
    answer = True
    
    num = 0
    for i in s:
        if i == "(":
            num += 1
        else:
            num -= 1
        if num < 0:
            answer = False
            break
    
    if num == 0:
        answer = True
    else:
        answer = False
    
    return answer