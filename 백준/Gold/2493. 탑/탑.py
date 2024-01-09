n = int(input())
l = list(map(int,input().split()))
s = []
d = {}
ans = [0] * n

for i in range(n):
    d[l[i]] = i
    
for i in range(n):
    while s:
        if s[-1] > l[i]:
            ans[i] = d[s[-1]] + 1
            break
        else:
            s.pop()
    s.append(l[i])
print(* ans)