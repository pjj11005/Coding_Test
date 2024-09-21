import sys
input = sys.stdin.readline

def solution(h, w, array):
  answer = 0
  for i in range(1, w - 1): # 양끝 제외(물이 채워질 수 있는 부분만 탐색)
    left = max(array[ :i]) # 왼쪽 부분의 최대
    right = max(array[i + 1: ]) # 오른쪽 부분의 최대
    m = min(left, right) # 그 두가지의 최소
    if m > array[i]:
        answer += m - array[i]
  return answer
h, w = map(int, input().split())
array = list(map(int, input().split()))
print(solution(h, w, array))