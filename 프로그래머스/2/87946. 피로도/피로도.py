from itertools import permutations
def solution(k, dungeons):
    answer = -1
    l = list(permutations(dungeons,len(dungeons)))
    
    for i in l:
        l2 = i
        tmp = k
        ttmp = 0
        for j in l2:
            a, b = j
            if tmp >= a:
                tmp -= b
                ttmp += 1
            else:
                break
        answer = max(answer, ttmp)
    return answer