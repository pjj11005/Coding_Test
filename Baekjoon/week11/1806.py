import sys
input = sys.stdin.readline

def solution(n, s, array):
  answer = 100000
  if array[0] >= s: # 초기값이 바로 조건 만족
    return 1
  start, end = 0, 0
  total = array[0] # 초기값
  while start <= end:
    if total >= s: # s 이상
      answer = min(answer, end - start + 1) # 최소 길이 갱신
      total -= array[start] # 앞의 값 제거
      start += 1 # 포인터 이동
    else:
      end += 1 # 뒤의 값으로 이동
      if end >= n: # 범위 벗어남
        break
      total += array[end] # 뒤의 값 더함

  if answer == 100000: # 조건 만족 안함
    return 0
  return answer

n, s = map(int, input().split())
array = list(map(int, input().split()))
print(solution(n, s, array))