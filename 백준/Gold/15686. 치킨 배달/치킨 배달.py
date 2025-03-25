import sys
input = sys.stdin.readline

n, m = map(int,input().split())
min_ans = int(1e9)
# 입력, 좌표 값 찾기
g = []
h, ch = [], []
s = [0] * m
com = []
for r in range(n):
    tmp = list(map(int,input().split()))
    g.append(tmp)
    for c in range(n):
        if tmp[c] == 1: # 집
            h.append((r, c)) # 세로, 가로
        if tmp[c] == 2: # 치킨집
            ch.append((r,c))

# m개 조합 구하기
def dfs(d, k):
    global m, min_ans
    if d == m:
        ttmp = 0
        for i in h:
            tmp = int(1e9)
            for j in s:
                tmp = min(tmp, abs(i[0] - j[0]) + abs(i[1] - j[1]))
            ttmp += tmp
        min_ans = min(min_ans, ttmp)
        return
    for i in range(k,len(ch)):
        s[d] = ch[i]
        dfs(d + 1, i + 1)

dfs(0,0)
print(min_ans)