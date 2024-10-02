import sys
input = sys.stdin.readline

def solution(array, num):
    answer = 0
    start, end = 0, len(array) - 1
    
    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        name, score = array[mid]
        if int(score) >= num:
            answer = name
            end = mid - 1
        else:
            start = mid + 1
    
    return answer 

n, m = map(int, input().split())
array = [list(input().split()) for _ in range(n)]
for i in range(m):
    num = int(input())
    print(solution(array, num))
    