import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(r, c, k, array):
  answer = 0
  # 초기에 바로 조건 만족
  if 1 <= r <= 3 and 1 <= c <= 3 and array[r - 1][c - 1] == k:
    return answer
  else:
    while True:
      temp = [] # 새로운 이차원 배열
      if len(array) >= len(array[0]): # R
        for row in array:
          count = defaultdict(int) # 숫자 개수 카운트
          num_list = [] # 새로운 행 혹은 열
          for i in row:
            if i != 0: # 1 이상의 자연수만 카운트
              count[i] += 1
          count_list = sorted(count.items(), key=lambda x:(x[1], x[0])) # 숫자와 횟수 리스트
          for a, b in count_list: # 저장
            num_list.append(a)
            num_list.append(b)
          temp.append(num_list)

        maxrow = max(len(row) for row in temp)
        if maxrow > 100: # 100개 초과
          for i in range(len(temp)):
            if len(temp[i]) <= 100:
              temp[i].extend([0] * (100 - len(temp[i])))
            else:
              temp[i] = temp[i][:100]
        else: # 100개 이하
          for i in range(len(temp)):
              temp[i].extend([0] * (maxrow - len(temp[i])))
        array = temp
      else: # P
        array = list(map(list, zip(*array))) # 전치
        for row in array:
          count = defaultdict(int) # 숫자 개수 카운트
          num_list = [] # 새로운 행 혹은 열
          for i in row:
            if i != 0: # 1 이상의 자연수만 카운트
              count[i] += 1
          count_list = sorted(count.items(), key=lambda x:(x[1], x[0])) # 숫자와 횟수 리스트
          for a, b in count_list: # 저장
            num_list.append(a)
            num_list.append(b)
          temp.append(num_list)

        maxrow = max(len(row) for row in temp)
        if maxrow > 100: # 100개 초과
          for i in range(len(temp)):
            if len(temp[i]) <= 100:
              temp[i].extend([0] * (100 - len(temp[i])))
            else:
              temp[i] = temp[i][:100]
        else: # 100개 이하
          for i in range(len(temp)):
              temp[i].extend([0] * (maxrow - len(temp[i])))
        array = list(map(list, zip(*temp))) # 전치

      answer += 1
      if 1 <= r <= len(array) and 1 <= c <= len(array[0]) and array[r - 1][c - 1] == k: # 최소 시간
        return answer

      if answer == 100: # 불가능
        return -1
        
r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]
print(solution(r, c, k, array))