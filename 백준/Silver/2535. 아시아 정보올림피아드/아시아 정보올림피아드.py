n = int(input())
l = []
d = {}
for i in range(100):
    d[i+1] = 0
for _ in range(n):
    nation, student, score = map(int,input().split())
    l.append((nation,student,score))

l = sorted(l,key=lambda x:x[2],reverse=True)

cnt = 0
for i in l:
    nation = i[0]
    student = i[1]
    if d[nation] >= 2:
        continue
    else:
        d[nation] += 1
        cnt += 1
        print("%d %d" %(nation,student))
    if cnt == 3:
        break