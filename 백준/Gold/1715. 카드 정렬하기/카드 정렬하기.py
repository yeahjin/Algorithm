import heapq
q = []
n = int(input())
for i in range(n):
    a = int(input())
    heapq.heappush(q,a)
l2 = []
while q:
    if len(q) == 1:
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, (a + b))
    l2.append(a+b)
print(sum(l2))
