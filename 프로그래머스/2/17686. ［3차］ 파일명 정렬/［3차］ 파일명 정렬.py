def solution(files):
    answer = []
    d = {}
    for i in files:
        tmp = ""
        flag = False
        tmp2 = ""
        for j in i.split(".")[0]:
            if not flag and not j.isdigit():
                tmp2 += j.lower()
            if j.isdigit():
                tmp += str(j)
                flag = True
            if flag and not j.isdigit():
                break
        d[i] = (int(tmp), tmp2)
    d = sorted(d.items(), key=lambda x:[x[1][1], x[1][0]])
    for name, lt in d:
        answer.append(name)
    return answer