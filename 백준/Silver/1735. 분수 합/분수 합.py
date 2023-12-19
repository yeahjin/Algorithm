import math
a, b = map(int,input().split())
c, d = map(int,input().split())

bottom = b * d // math.gcd(b,d)

top = bottom//b * a + bottom//d * c

print(top//math.gcd(bottom,top), bottom//math.gcd(bottom,top))