import sys
input = sys.stdin.readline

def solution(n, m , array):
    answer = max(array[0], n - array[m - 1]) # 양 끝 거리 중 최대
    for i in range(1, m):
        if (answer * 2) < (array[i] - array[i - 1]): # 가로등 사이 비추기 X
            if (array[i] - array[i - 1]) % 2 == 1: # 홀수
                answer = ((array[i] - array[i - 1]) // 2) + 1
            else: # 짝수
                answer = ((array[i] - array[i - 1]) // 2)
    return answer

n = int(input())
m = int(input())
array = list(map(int, input().split()))
print(solution(n, m, array))