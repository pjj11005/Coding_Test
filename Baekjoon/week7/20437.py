import sys
input = sys.stdin.readline

def solution(w, k):
  index = {}
  minimum, maximum = int(1e9), 0 # 최소값, 최대값
  # 문자별 각 인덱스 위치 리스트로 저장
  for i, word in enumerate(w):
    index[word] = index.get(word, [])
    index[word].append(i)
  # 문자별로 각 최소, 최대 연속 k개 문자열 길이 확인
  for word, index_list in index.items():
    if len(index_list) >= k:
      for i in range(len(index_list) - k + 1):
        length = index_list[i + k - 1] - index_list[i] + 1
        minimum = min(minimum, length)
        maximum = max(maximum, length)
  # 정답 return
  if minimum == int(1e9) and maximum == 0:
    return print(-1)
  else:
    return print(minimum, maximum)
      
for _ in range(int(input())):
  w = list(input().strip())
  k = int(input())
  solution(w, k)