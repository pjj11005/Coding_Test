import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort()

    total, time, idx = 0, 0, 0
    temp = []

    while idx < n or temp:  # 모든 작업 완료 시까지
        while idx < n and jobs[idx][0] <= time:  # 현재 시간 이전 작업 모두 처리
            heapq.heappush(temp, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if temp:  # 작업 수행
            spend, require = heapq.heappop(temp)
            time += spend
            total += time - require
        else:  # 작업 없으면 다음 요청 시간으로 점프
            time = jobs[idx][0]

    return total // n