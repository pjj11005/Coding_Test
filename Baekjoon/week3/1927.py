import sys
import heapq

input = sys.stdin.readline

def solution(n):
    q = []
    for i in range(n):
        num = int(input())
        if num == 0: # 연산
            if len(q): # 값 존재
                print(heapq.heappop(q))
            else: # 값 없음
                print(0)
        else: # 입력
            heapq.heappush(q, num)

n = int(input())
solution(n)