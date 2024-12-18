import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def solution(heap, count, is_max=False):
    while heap:
        num = heapq.heappop(heap)
        if is_max: # 최대 힙
            num = -num
        # 개수가 있는 요소를 발견할 때까지
        if count[num] > 0: 
            count[num] -= 1
            return num
    return None

for _ in range(int(input())):
    min_heap, max_heap = [], [] # 최소 힙, 최대 힙
    count = defaultdict(int) # 요소의 개수
    max_val, min_val = 0, 0
    for _ in range(int(input())):
        op, n = input().strip().split()
        n = int(n)
        # 삽입
        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            count[n] += 1
        # 삭제
        else:
            if n == 1: # 최대 삭제
                max_val = solution(max_heap, count, True)
            else: # 최소 삭제
                min_val = solution(min_heap, count)
                
    max_val = solution(max_heap, count, True)
    # empty
    if max_val is None:
        print('EMPTY')
    else:
        count[max_val] += 1 # 다시 추가
        min_val = solution(min_heap, count)
        print(max_val, max_val if min_val is None else min_val)