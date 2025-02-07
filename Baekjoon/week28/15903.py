import sys
import heapq

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    answer = sum(array)
    
    q = []  # 최소 힙
    for i in array:
        heapq.heappush(q, i)
    
    # 최소 카드 합 계산
    for _ in range(m):
        x1 = heapq.heappop(q)
        x2 = heapq.heappop(q)
        answer += x1 + x2
        heapq.heappush(q, x1 + x2)
        heapq.heappush(q, x1 + x2)
    
    print(answer)


if __name__ == '__main__':
    solution()
