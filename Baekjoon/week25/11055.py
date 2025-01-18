import sys

input = sys.stdin.readline


def solution():
  n = int(input())
  array = list(map(int, input().split()))
  # dp = arr[:]  # 배열 복사 방법도 있음
  dp = [i for i in array]  # 해당 수까지 가장 큰 증가하는 부분 수열의 합

  for i in range(1, n):
    for j in range(i):
      # 앞의 수보다 크면 dp 갱신
      if array[i] > array[j]:
        dp[i] = max(dp[i], dp[j] + array[i])

  print(max(dp))


if __name__ == '__main__':
  solution()
