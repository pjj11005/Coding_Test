import sys

input = sys.stdin.readline
INF = int(1e9)


def solution():
  n = int(input())
  dp = [1] * (n + 1)  # dp[i] : 실제로 2 * i를 만드는 개수
  n >>= 1  # n을 2로 나눈 몫

  for i in range(1, n + 1):
    dp[i] = dp[i - 1] + dp[i >> 1]  # 이전의 경우의 수 + 2로 나눈값의 경우의 수
    if dp[i] >= INF:
      dp[i] -= INF

  print(dp[n])


if __name__ == '__main__':
  solution()
