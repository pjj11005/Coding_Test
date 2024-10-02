import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(n, array):
  minimum = INF * 2
  a, b = 0, 0
  left, right = 0, n - 1
  while left < right:
    total = array[left] + array[right]
    if total >= 0: # 양수 + 0
      if minimum >= total: # 값 저장
        minimum = total
        a, b = array[left], array[right]
      right -= 1
    else: # 음수
      if minimum >= -total: # 값 저장
        minimum = -total
        a, b = array[left], array[right]
      left += 1
  return print(a, b)
  
n = int(input())
array = list(map(int, input().split()))
solution(n, array)