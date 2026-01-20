from itertools import combinations
while True:
    a = list(map(str,input().split()))
    if a[0] == '0':
        break
    comb = combinations(a[1:],6)
    for i in comb:
        print(" ".join(i))
    print()