import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1,int(math.sqrt(total))+1):
        if total % i == 0:
            a = total//i
            b = i
            if a * 2 + (b-2) * 2 == brown:
                answer.append(max(a,b))
                answer.append(min(a,b))
    
    return answer