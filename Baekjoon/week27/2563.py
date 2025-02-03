import sys

input = sys.stdin.readline


def solution():
  n = int(input())
  array = [[0] * 100 for _ in range(100)]  # 각 지점 체크

  # 중복되지 않게 검은 부분 체크
  for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
      for j in range(y, y + 10):
        array[i][j] = 1

  print(sum(sum(row) for row in array))


if __name__ == '__main__':
  solution()
