import sys

input = sys.stdin.readline
INF = int(1e9)


def dfs(cur, visited, n, array, dp):
  # n개 행성 모두 방문
  if visited == (1 << n) - 1:
    return 0

  # 저장된 값이 존재
  if dp[cur][visited] != -1:
    return dp[cur][visited]

  dp[cur][visited] = INF
  
  # 지나가지 않은 경로로 지나감
  for i in range(n):
    # 방문한 곳은 스킵
    if visited & (1 << i):
      continue
    # 방문 안한 곳 방문
    dp[cur][visited] = min(dp[cur][visited], array[cur][i] + dfs(i, visited | (1 << i), n, array, dp))

  return dp[cur][visited]

def solution():
  n, k = map(int, input().split())
  array = [list(map(int, input().split())) for _ in range(n)]

  # 각 경로 최소 시간 구하기
  for x in range(n):
    for start in range(n):
      for end in range(n):
        if start == end:
          continue
        array[start][end] = min(array[start][end],
                                array[start][x] + array[x][end])

  # 각 방문 상태에 대한 최소 시간 저장
  dp = [[-1] * (1 << n) for _ in range(n)]

  print(dfs(k, 1 << k, n, array, dp))


if __name__ == '__main__':
  solution()
