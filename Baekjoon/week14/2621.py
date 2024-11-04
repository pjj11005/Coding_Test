import sys
input = sys.stdin.readline
 
def solution(colors, nums):
  answer = 0
  if len(set(colors)) == 1: # 색깔 하나
    if sorted(nums) == [min(nums), min(nums) + 1, min(nums) + 2, min(nums) + 3, min(nums) + 4]: # 1번
      answer = max(answer, 900 + max(nums))
    else: # 4번
      answer = max(answer, 600 + max(nums))

  if sorted(nums) == [min(nums), min(nums) + 1, min(nums) + 2, min(nums) + 3, min(nums) + 4]: # 5번
    answer = max(answer, 500 + max(nums))
    
  num_list = list(set(nums)) # 중복되지 않은 숫자
  count_list = [] # 개수
  for n in num_list:
    count_list.append(nums.count(n))
    
  if 4 in count_list: # 2번
    idx = count_list.index(4)
    answer = max(answer, 800 + num_list[idx])
    
  if 3 in count_list:
    idx = count_list.index(3)
    if len(count_list) == 2: # 3번
      idx2 = 1 - idx
      answer = max(answer, 700 + (num_list[idx] * 10) + num_list[idx2])
    # 6번
    answer = max(answer, 400 + num_list[idx])
    
  if sorted(count_list) == [1, 2, 2]: # 7번
    n_list = []
    for i, c in enumerate(count_list):
      if c == 2:
        n_list.append(num_list[i])
    answer = max(answer, 300 + (max(n_list) * 10) + min(n_list))
    
  if 2 in count_list:
    idx = count_list.index(2)
    answer = max(answer, 200 + num_list[idx])

  if answer == 0: # 9번
    answer = max(answer, 100 + max(nums))
    
  return answer
  
colors = []
nums = []
for i in range(5):
  color, num = input().split()
  colors.append(color)
  nums.append(int(num))
print(solution(colors, nums))