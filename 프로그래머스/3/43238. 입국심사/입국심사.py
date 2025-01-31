def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in times:
            total += mid // i
        if total < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
        
    return answer