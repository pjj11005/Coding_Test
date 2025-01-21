import sys

input = sys.stdin.readline


def solution():
  n, m = map(int, input().split())
  men = sorted(list(map(int, input().split())))
  women = sorted(list(map(int, input().split())))

  # dp[i][j]: i번째 남자까지, j번째 여자까지 고려했을 때의 최소 성격 차이 합
  dp = [[0] * (m + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if i == j:  # 남녀 수가 같은 경우
        dp[i][j] = dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1])
      elif i > j:  # 남자가 더 많은 경우
        dp[i][j] = min(dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1]), # 현재 남자 포함
                       dp[i - 1][j]) # 현재 남자 고려 안함
      else:  # 여자가 더 많은 경우
        dp[i][j] = min(dp[i - 1][j - 1] + abs(men[i - 1] - women[j - 1]), # 현재 여자 포함
                       dp[i][j - 1]) # 현재 여자 고려 안함

  print(dp[n][m])


if __name__ == '__main__':
  solution()
