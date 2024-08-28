import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    array = list(map(int, input().split()))
    idx = 0
    answer = 0
    while True:
        maximum = max(array)
        idx = len(array) - 1 - array[::-1].index(maximum) # maximum 값들 중에서 마지막

        if idx > 0:  # maximum 앞의 수들 과의 차이 더해줌
            answer += (maximum * idx) - sum(array[:idx])

        if idx == n - 1: # 마지막 요소가 maximum
            return answer
        
        idx += 1
        array = array[idx:]
        if len(array) <= 1:
            return answer

t = int(input())
for i in range(t):
    print(solution())