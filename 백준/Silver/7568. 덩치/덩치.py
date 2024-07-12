import sys

l = []

n = int(input())
for i in range(n):
    weight, height = map(int,sys.stdin.readline().split())
    l.append([weight,height])

for i in l:
    rank = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")