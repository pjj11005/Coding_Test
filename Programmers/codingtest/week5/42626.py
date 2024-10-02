import heapq

def solution(scoville, K):
    answer = 0
    q = sorted(scoville)
    while True:
        if len(q) == 1:  # 길이 1
            if q[0] >= K:
                break
            else:
                answer = -1
                break
        else:
            if q[0] >= K:
                break
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            num = a + (2 * b)
            heapq.heappush(q, num)
        answer += 1
    return answer