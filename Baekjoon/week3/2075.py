import sys
import heapq

input = sys.stdin.readline

def solution():
    n = int(input())
    q = []
    for i in range(n):
        array = list(map(int, input().split()))
        if not q: # 초기
            for a in array:
                heapq.heappush(q, a)
        else: # 존재할 때
            for a in array:
                if a > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q, a)
    return q[0]

print(solution())
