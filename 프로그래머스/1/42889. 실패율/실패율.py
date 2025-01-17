def solution(N, stages):
    answer = []
    l = [0] * (N+2)
    for i in stages:
        l[i] += 1
    # 도전자 수
    p = [0] * (N + 1)
    p[1] = sum(l)
    for i in range(2,N+1):
        p[i] = p[i-1] - l[i-1]
    # 통계 계산
    a = []
    for i in range(1,N+1):
        if l[i] == 0 or p[i] == 0:
            a.append((i,0))
            continue
        a.append((i,l[i]/p[i]))
    # 정렬
    a = sorted(a,key=lambda x:[-x[1],x[0]])
    ans = []
    for i in a:
        ans.append(i[0])
    return ans 