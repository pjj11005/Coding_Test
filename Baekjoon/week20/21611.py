import sys
from itertools import groupby
input = sys.stdin.readline

# 이차원 배열 -> list
def array_to_list(array):
	count = 1 # 이동 반복 횟수
	x, y = n//2, n//2 # 상어 위치
	result = []
	while True:
		if count % 2 == 1:
			move = [(0, -1), (1, 0)]
		else:
			move = [(0, 1), (-1, 0)]
		
		for dx, dy in move:
			for _ in range(count):
				nx, ny = x + dx, y + dy
				if 0 <= nx < n and 0 <= ny < n:
					if array[nx][ny] == 0: # 끝
						return result
					else:
						result.append(array[nx][ny])
						x, y = nx, ny
				else: # 범위 밖
					return result
		
		count += 1

# 블리자드
def blizzard(d, s, stack):
	global answer
	
	# 파괴할 초기 인덱스 설정
	if d == 1:
		num = 6
	elif d == 2:
		num = 2
	elif d == 3:
		num = 0
	else:
		num = 4
	plus = num # 더해나갈 값
	
	for i in range(s):
		if num < len(stack): # 범위 이내
			del stack[num]
		else: # 범위 넘으면 종료
			break
		plus += 8
		num += plus
	
	while True:
		explosion = False # 폭발한 구슬 유무
		grouped = [list(group) for _, group in groupby(stack)]

		transformed = []
		for group in grouped:
			if len(group) >= 4:
				if not explosion:
					explosion = True
				answer += (len(group) * group[0])
			else:
				transformed.extend([group[0]] * len(group))
		
		stack = transformed
		
		# 폭발한게 없음
		if not explosion:
			break
	
	# 그룹화
	grouped = [list(group) for _, group in groupby(stack)]

	transformed = []
	for group in grouped:
		transformed.extend([len(group), group[0]])
	
	return transformed[:(n * n) - 1] # 상어 위치 뺴고 배열의 최대 길이는 (n X n) - 1
		
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
stack = array_to_list(array) # 구슬 리스트
answer = 0 # 답

for _ in range(m):
	d, s = map(int, input().split())
	stack = blizzard(d, s, stack)

print(answer)