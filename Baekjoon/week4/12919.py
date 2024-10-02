import sys
from collections import deque

input = sys.stdin.readline

def solution(s, t):
  q = deque([t])
  visited = set()
  visited.add(t)
  while q:
    string = q.popleft()
    if string == s:  # 가능
      return 1

    # (A_____B) : 불가능
    if string[-1] == 'A' and string[0] == 'A':  # (A_____A) : A 추가
      new_string = string[:-1]
      if len(new_string) >= len(s) and new_string not in visited:
        visited.add(new_string)
        q.append(new_string)
    elif string[-1] == 'B' and string[0] == 'B':  # (B_____B) : B 추가
      new_string = string[::-1]
      new_string = new_string[:-1]
      if len(new_string) >= len(s) and new_string not in visited:
        visited.add(new_string)
        q.append(new_string)
    elif string[-1] == 'A' and string[0] == 'B':  # (B_____A) : A 추가 or B추가
      for i in range(2):
        if i == 0:  # A 추가
          new_string = string[:-1]
          if len(new_string) >= len(s) and new_string not in visited:
            visited.add(new_string)
            q.append(new_string)
        else:  # B 추가
          new_string = string[::-1]
          new_string = new_string[:-1]
          if len(new_string) >= len(s) and new_string not in visited:
            visited.add(new_string)
            q.append(new_string)
  return 0

s = input().strip()
t = input().strip()
print(solution(s, t))

'''
- S를 T로 바꾸는 BFS로는 메모리 초과 발생
- 따라서, T를 S로 바꾸는 BFS로 해결 → 방법의 가짓수가 줄어든다
- 항상 역방향으로 계산하는 경우도 고려해야함
'''