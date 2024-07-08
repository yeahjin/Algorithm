n, k = map(int,input().split())
cnt = 0
is_prime = [True] * (n+1)
for i in range(2,n+1):
    if is_prime[i]:
        for j in range(i, n+1, i):
            if is_prime[j]:
                cnt += 1
                is_prime[j] = False
            if cnt == k:
                print(j)
                break
