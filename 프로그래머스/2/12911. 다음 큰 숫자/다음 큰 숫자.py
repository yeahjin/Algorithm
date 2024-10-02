def solution(n):
    answer = 0
    
    for i in range(n+1, 1048576):
        if bin(n).count("1") == bin(i).count("1"):
            return i