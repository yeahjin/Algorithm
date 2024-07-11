import sys

d = {}
total = 0
try:
    while True:
        s = sys.stdin.readline().rstrip()
        if s == "":
            break
        if s not in d:
            total += 1
            d[s] = 1
        else:
            total += 1
            d[s] += 1
except EOFError:
    pass
d2 = {}
for i in d.items():
    d2[i[0]] = (i[1] / total)*100

d2 = sorted(d2.items(), key = lambda x: x[0])

for name, per in d2:
    print("%s %.4f" %(name,per))