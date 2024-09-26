import sys
input = sys.stdin.readline

def solution(n, array):
    array.sort()
    answer = 0
    for i in range(n): # 모든 원소를 한번씩 목표로 지정
        goal = array[i]
        start = 0
        end = len(array)-1
        while start < end: # 포인터 두개로 범위 줄이며 탐색
            if array[start] + array[end] == goal:
                if start == i:
                    start += 1
                elif end == i:
                    end -= 1
                else:
                    answer += 1
                    break
            elif array[start] + array[end] > goal:
                end -= 1
            elif array[start] + array[end] < goal:
                start += 1
    return answer
n = int(input())
array = list(map(int, input().split()))
print(solution(n, array))