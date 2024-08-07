import sys
input = sys.stdin.readline

def move_element(lst, from_index, to_index):
  element = lst.pop(from_index)  # 이동할 요소를 리스트에서 제거
  lst.insert(to_index, element)  # 해당 요소를 새로운 위치에 삽입
  return lst

p = int(input())
for _ in range(p):
  count = 0
  temp = list(map(int, input().split()))
  t = temp[0]
  array = temp[1:]
  for i in range(1, 20):
    for j in range(i):
      if array[j] > array[i]:  # 자기보다 큰 가장 앞에 있는 애 발견
        count += i - j
        move_element(array, i, j)
  print(t, count)
