import sys
input = sys.stdin.readline

b = int(input()) # 판단 데이터 수
low, high = [], []

for i in range(b):
    low.append(input().strip())

for i in range(b):
    high.append(input().strip())

n = int(input())
l = []
for i in range(n):
    l.append(input().strip())

for case in l:
    hh = 0
    ll = 0
    for h in high:
        for i in range(len(case)-len(h)+1):
            if case[i:i+len(h)] == h:
                hh += 1
    for lo in low:
        for i in range(len(case) - len(lo) + 1):
            if case[i:i + len(lo)] == lo:
                ll += 1
    c = hh - ll
    if c > 0:
        print("LOW %d" %(abs(c)))
    elif c < 0:
        print("HIGH %d" % (abs(c)))
    else:
        print("GOOD")