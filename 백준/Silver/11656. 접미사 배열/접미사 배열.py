s = input()
l = []

for i in range(len(s)-1,-1,-1):
    l.append(s[i:len(s)])
l.sort()
for i in l:
    print(i)