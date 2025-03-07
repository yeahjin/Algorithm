def union(a,b,p):
    a = find(a,p)
    b = find(b,p)
    if a < b:
        p[b] = a
    else:
        p[a] = b
        
def find(x,p):
    if x != p[x]:
        p[x] = find(p[x],p)
    return p[x]

def solution(n, computers):
    answer = 0
    p = [i for i in range(n+1)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                union(i+1,j+1,p)
    s = set()
    for i in p[1:]:
        s.add(find(i,p))
    
    return len(s)