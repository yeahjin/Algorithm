def solution(s):
    answer = True
    l = []
    
    for i in s:
        if i == "(":
            l.append(i)
        else:
            if len(l) <= 0:
                return False
            l.pop()
    
    if len(l) == 0:
        return True
    else:
        return False