import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    name, ko, en, ma = map(str,input().split())
    l.append((name,int(ko),int(en),int(ma)))
# 이름 사전 순
l = sorted(l, key=lambda x:x[0])
# 수학 점수 감소
l = sorted(l, key=lambda x:x[3], reverse=True)
# 영어 성적 증가
l = sorted(l, key= lambda x:x[2])
# 국어 성적 감소
l = sorted(l, reverse= True ,key=lambda x:x[1])


for i in l:
    print(i[0])