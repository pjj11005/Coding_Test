import sys
input = sys.stdin.readline

def count(array):
  cnt = 0 # 누울 자리 수
  for row in array:
    i = 0 # 인덱스
    length = 0 # '.'의 길이
    while True:
      if row[i] == '.':
        length += 1
      else:
        if length >= 2:
          cnt += 1
        length = 0
      i += 1
      if i == n:
        if length >= 2:
          cnt += 1
        break
  return cnt
  
def solution(n, array):
  cnt1 = count(array)
  cnt2 = count(list(map(list, zip(*array))))
  print(cnt1, cnt2)
  
n = int(input())
array = [list(input().strip()) for _ in range(n)]
solution(n, array)