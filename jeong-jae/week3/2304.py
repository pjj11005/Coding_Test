import sys
input = sys.stdin.readline

def solution(n, array):
    answer = 0
    array = sorted(array, key=lambda x:-x[1])
    left, right = array[0][0], array[0][0] # 위치
    answer += array[0][1] # 가장 높은 막대 너비 추가

    for i in range(1, n):
        if array[i][0] < left: # 왼쪽 요소
            answer += (left - array[i][0]) * array[i][1]
            left = array[i][0]
        elif array[i][0] > right: # 오른쪽 요소
            answer += (array[i][0] - right) * array[i][1]
            right = array[i][0]
    return answer

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, array))