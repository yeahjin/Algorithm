def union(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def find(p,x):
    if p[x] != x:
        p[x] = find(p,p[x])
    return p[x]
    
def solution(n, costs):
    answer = 0
    p = [i for i in range(n)]
    
    costs = sorted(costs,key=lambda x:x[2])
    
    for a, b, c in costs:
        if find(p,a) != find(p,b):
            union(p,a,b)
            answer += c
    
    return answer