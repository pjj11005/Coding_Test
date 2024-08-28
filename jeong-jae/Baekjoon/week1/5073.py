import sys
input = sys.stdin.readline

while True:
  temp = list(map(int, input().split()))
  if sum(temp) == 0:  # 종료
    break
  
  temp.sort(reverse=True)
  if temp[0] >= temp[1] + temp[2]: # Invalid
    print('Invalid')
  elif temp[0] == temp[1] and temp[1] == temp[2] and temp[0] == temp[2]: # Equilateral
    print('Equilateral')
  elif temp[0] == temp[1] or temp[1] == temp[2] or temp[0] == temp[2]: # Isosceles
    print('Isosceles')
  else: # Scalene 
    print('Scalene ')