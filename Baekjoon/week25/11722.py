import sys

input = sys.stdin.readline


def solution():
  n = int(input())
  array = list(map(int, input().split()))
  dp = [1] * n  # 해당 수까지 가장 긴 감소하는 부분 수열의 길이

  for i in range(1, n):
    for j in range(i):
      # 앞의 수보다 작으면 dp 갱신
      if array[i] < array[j]:
        dp[i] = max(dp[i], dp[j] + 1)

  print(max(dp))


if __name__ == '__main__':
  solution()
