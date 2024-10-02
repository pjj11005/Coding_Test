def solution(distance, rocks, n):
    answer = 0
    start, end = 0, int(1e9)
    m = len(rocks) - n
    rocks.sort()
    while start <= end:
        mid = (start + end) // 2
        
        count = 0
        s_rock = 0
        for rock in rocks:
            if rock - s_rock >= mid:
                count += 1
                s_rock = rock
        
        if distance - s_rock < mid: # 마지막 돌과 도착지점사이 거리가 최소보다 작을 때
            count -= 1
        
        if count < m:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer