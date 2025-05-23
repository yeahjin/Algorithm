import sys
input = sys.stdin.readline

n, m = map(int,input().split())
g = []

# 모든 테트로미노
tetromino_shapes = [
    # ㅡ
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],

    # ㅁ
    [(0,0), (0,1), (1,0), (1,1)],

    # ㄴ 모양
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (1,0), (2,0)],

    # ㄱ 대칭
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (0,1), (0,2), (1,0)],

    # 번개 모양
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,0), (1,0), (1,1), (2,1)],

    # ㅗ 모양
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(0,1), (1,1), (2,1), (1,0)],
]

for i in range(n):
    tmp = list(map(int,input().split()))
    g.append(tmp)
max_num = -1
for y in range(n):
    for x in range(m):
        for s in tetromino_shapes:
            total = 0
            for dx, dy in s:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < m and 0 <= ny < n:
                    total += g[ny][nx]
                max_num = max(max_num, total)
print(max_num)