import sys

input = sys.stdin.readline


def dfs(idx, first, second, n, m, open, dp):
  if idx == m:
    return 0

  # 이미 값이 존재
  if dp[idx][first][second] != -1:
    return dp[idx][first][second]

  dp[idx][first][second] = min(abs(open[idx] - first) + dfs(idx + 1, open[idx], second, n, m, open, dp), # 첫번째 쪽으로 밀기
                              abs(open[idx] - second) + dfs(idx + 1, first, open[idx], n, m, open, dp)) # 두번째 쪽으로 밀기
  
  return dp[idx][first][second]


def solution():
  n = int(input())
  x, y = map(int, input().split())
  m = int(input())
  open = [int(input()) for _ in range(m)]
  dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(m)]  # dp[idx][door1][door2] : idx번째 사용해야할 때 최소 이동 횟수(열린 곳은 door1, door2)

  print(dfs(0, x, y, n, m, open, dp))


if __name__ == '__main__':
  solution()
