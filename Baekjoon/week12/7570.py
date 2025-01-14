import sys

input = sys.stdin.readline


def solution():
  n = int(input())
  array = list(map(int, input().split()))

  # 각 숫자까지의 연속 증가 수열 -> 1씩 증가하는 수열
  dp = [0] * (n + 1)

  # 최소 이동 횟수 계산
  for i in range(n):
    current = array[i]
    # 현재의 수 보다 1 작은 수가 앞에 있으면 그 수 까지 증가수열 길이 + 1
    dp[current] = dp[current - 1] + 1

  # 최소 이동 횟수 = 전체 길이 - 가장 긴 연속 증가 수열의 길이
  print(n - max(dp))


if __name__ == '__main__':
  solution()
