def solution(number, k):
    answer = []
    
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            k -= 1
            answer.pop()
        answer.append(i)
    
    if k > 0:
        answer = answer[:-k]
    
    
    return "".join(answer)