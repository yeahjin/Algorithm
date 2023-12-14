import sys

n = 0

visited = []
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, -1, 1, 1, -1]

r = []
a = []
b = []

def main():
    global n
    global cnt
    cnt = 0
    n = int(input())
    for i in range(n):
        r.append(False)
    for i in range(2*n-1):
        a.append(False)
        b.append(False)
    dfs(0)
    print(cnt)

def dfs(idx):
    global cnt
    if idx == n:
        cnt+=1
        return
    for i in range(n):
        if r[i] == True or a[idx + i] == True or b[idx-i] == True:
            continue
        r[i] = True
        a[idx+i] = True
        b[idx-i] = True
        dfs(idx+1)
        r[i] = False
        a[idx+i] = False
        b[idx-i] = False

if __name__ == "__main__":
    main()