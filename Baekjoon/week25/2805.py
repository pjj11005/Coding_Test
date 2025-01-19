import sys
from collections import Counter
input = sys.stdin.readline


def binary_search(m, array):
  answer = 0
  start, end = 0, int(1e9)

  # 이진 탐색
  while start <= end:
    mid = (start + end) >> 1 # 비트 연산

    # m 이상의 길이
    if sum((h - mid) * c for h, c in array if h > mid) >= m:
      answer = mid
      start = mid + 1
    else:
      end = mid - 1

  return answer


def solution():
  n, m = map(int, input().split())
  array = list(Counter(map(int, input().split())).items()) # (높이, 개수)로 저장
  print(binary_search(m, array))


if __name__ == '__main__':
  solution()
