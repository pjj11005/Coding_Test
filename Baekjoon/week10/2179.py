import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(n, array):
  count = defaultdict(int) # 가능한 접두어 들의 개수
  max_prefix, max_length = '', 0 # 최장 접두어, 최장 길이
  answer = [] # 정답
  # 각 단어 별로 가능한 접두어 개수 증가
  for a in array:
    tmp = ''
    for i in a:
      tmp += i
      count[tmp] += 1
  # 최장 접두어 및 길이 찾기
  for word, count in count.items():
    if count >= 2 and len(word) > max_length: # 2개 이상이고 길이 길 때
        max_prefix, max_length = word, len(word)
      
  # 가장 빠른 두 단어 찾기
  cnt = 0
  for a in array:
    if cnt == 2: # 두개 찾음
      break
    if a[:max_length] == max_prefix: # 최장 접두어 가능
      cnt += 1
      answer.append(a)

  print(answer[0])
  print(answer[1])
  
n = int(input())
array = [input().strip() for _ in range(n)]
solution(n, array)

''' 내 풀이 : 7556ms
import sys
input = sys.stdin.readline

def solution(n, array):
  answer = -1 # 최대 접두어 길이
  s, t = '', '' # s, t
  s_idx, t_idx = 0, 0
  q = []
  for i in range(n): # 단어, 인덱스 저장
    q.append([array[i], i])
  q.sort()

  for i in range(n - 1):
    for j in range(i + 1, n):
      if answer >= 0 and q[i][0][0] != q[j][0][0]: # answer 0 이상인 후 시작 부분이 다르면 그 뒤로 탐색할 필요 없음
        break
      
      if q[i][1] < q[j][1]:
        str1, idx1 = q[i]
        str2, idx2 = q[j]
      else:
        str1, idx1 = q[j]
        str2, idx2 = q[i]

      # 접두어 공통 길이 비교
      count = 0
      m = min(len(str1), len(str2))
      for k in range(m):
        if str1[k] != str2[k]:
          break
        count += 1
      if count > answer:
        answer = count
        s, t = str1, str2
        s_idx, t_idx = idx1, idx2
      elif count == answer:
        if s_idx > idx1:
          s, t = str1, str2
          s_idx, t_idx = idx1, idx2
        elif s_idx == idx1 and t_idx > idx2:
          s, t = str1, str2
          s_idx, t_idx = idx1, idx2
      
  print(s)
  print(t)
          
n = int(input())
array = [input().strip() for _ in range(n)]
solution(n, array)
'''