def solution(n, times):
    answer = int(1e18)
    start, end = 0, int(1e18)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for t in times:
            count += mid // t
        
        if count < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = min(answer, mid)
    return answer