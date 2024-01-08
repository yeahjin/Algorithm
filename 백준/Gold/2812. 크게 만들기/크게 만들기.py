n, k = map(int,input().split())
s = input()
l = []
for i in s:
    while l and l[-1] < int(i) and k > 0:
        l.pop()
        k-=1
    l.append(int(i))
if k > 0:
    for i in range(len(l)-k):
        print(l[i],end='')
else:
    for i in l:
        print(i,end='')