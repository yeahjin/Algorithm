import sys
input = sys.stdin.readline

def find(x):
    global parent
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
parent = []
for i in range(n+1):
    parent.append(i)

l = []
for i in range(n):
    l.append(list(map(int,input().split())))

l2 = list(map(int,input().split()))
edge = []
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            edge.append((i+1,j+1))


for x, y in edge:
    union(x,y)

for i in range(1,len(parent)):
    parent[i] = find(parent[i])

tmp = True
for i in range(1,len(l2)):
    if parent[l2[i]] != parent[l2[i-1]]:
        tmp = False
        break
print("YES" if tmp else "NO")