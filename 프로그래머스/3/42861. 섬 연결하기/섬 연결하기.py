def solution(n, costs):
    answer = 0
    p = [0] * n
    for i in range(n):
        p[i] = i
    
    costs.sort(key=lambda x:x[2])

    result = 0
    for a,b,c in costs:
        if find(p,a) != find(p,b):
            union(p,a,b)
            result += c
    return result

def find(p,x):
    if p[x] != x:
        return find(p,p[x])
    return x

def union(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b