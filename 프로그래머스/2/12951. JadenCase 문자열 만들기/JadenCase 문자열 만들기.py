def solution(s):
    l = s.split(" ")
    answer = []
    for i in l:
        answer.append(i.capitalize())
    return " ".join(answer)