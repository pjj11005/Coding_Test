import sys
input = sys.stdin.readline

def solution(n, array):
  answer = [0] * n # 수신 리스트
  temp = [] # 임시 저장 리스트
  index = n - 1
  while array:
    if not temp:
      num = array.pop()
      temp.append([num, index])
      index -= 1
    
    num = array.pop()
    while temp:
      n, i = temp.pop()
      if n < num:
        answer[i] = index + 1
      else:
        temp.append([n, i])
        break
    temp.append([num, index])
    index -= 1
        
  for a in answer:
      print(a, end=' ')

n = int(input())
array = list(map(int, input().split()))
solution(n, array)