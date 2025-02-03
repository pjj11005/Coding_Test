import sys
from collections import defaultdict

input = sys.stdin.readline


def find_num(i, A, p, q, x, y):
  if i <= 0:  # 0 이하
    return 1
  else:  # 1 이상
    if A[i]:  # 이미 알고 있음
      return A[i]
    else:  # 찾아야 함
      num1 = 1 if (i // p) - x <= 0 else find_num((i // p) - x, A, p, q, x, y)
      num2 = 1 if (i // q) - y <= 0 else find_num((i // q) - y, A, p, q, x, y)
      A[i] = num1 + num2
    return A[i]


def solution():
  n, p, q, x, y = map(int, input().split())
  A = defaultdict(int)
  print(find_num(n, A, p, q, x, y))


if __name__ == '__main__':
  solution()
