import sys
input = sys.stdin.readline

def solution(n, array):
  dp = [1] * n # dp[i] : i번째 요소까지의 가장 긴 증가하는 부분 수열
  for i in range(1, n):
    for j in range(i):
      if array[j] < array[i]:
        dp[i] = max(dp[i], dp[j] + 1)
  return n - max(dp) # 현재 배열에서 가장 긴 증가하는 부분 수열의 요소들 제외하고 나머지 점프 시킴
    
n = int(input())
array = [int(input()) for _ in range(n)]
print(solution(n, array))
