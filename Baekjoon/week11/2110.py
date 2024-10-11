import sys
input = sys.stdin.readline

def solution(n, c, array):
  answer = 0
  start, end = 1, max(array)
  while start <= end:
    mid = (start + end) // 2
    count = 1
    pivot = array[0] # 초기값
    for a in array[1:]:
      if a - pivot >= mid:
        pivot = a
        count += 1
    
    if count < c: # 최소 간격 감소
      end = mid - 1
    else: # 최소 간격 증가 + answer 갱신
      start = mid + 1
      answer = max(answer, mid)
    
  return answer

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()  # 정렬
print(solution(n, c, array))