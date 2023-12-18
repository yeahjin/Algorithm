import math
a, b = map(int,input().split())
tmp = math.gcd(a,b)
print(a//tmp * b//tmp * tmp)