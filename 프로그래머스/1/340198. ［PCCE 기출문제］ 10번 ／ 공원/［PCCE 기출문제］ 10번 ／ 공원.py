def solution(mats, park):
    answer = -1
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] != "-1":
                continue
            answer = max(mats_sol(mats,park, i, j),answer)
    
    
    return answer

def mats_sol(mats, park, i, j):
    h = len(park)
    w = len(park[0])
    ans = -1
    for s in mats:
        flag = False
        for x in range(s):
            for y in range(s):
                ni = x + i
                nj = y + j
                if ni < 0 or ni >= h or nj <0 or nj >= w:
                    flag = True
                    continue
                if park[ni][nj] != "-1":
                    flag = True
                    continue
        if flag:
            continue
        ans = max(ans, s)
    return ans