def hanoi(n,s,m,e):
    if n == 1:
        print("%d %d" %(s,e))
        return
    hanoi(n-1,s,e,m)
    print("%d %d" %(s,e))
    hanoi(n-1,m,s,e)
n = int(input())
print(2**n-1)
hanoi(n,1,2,3)