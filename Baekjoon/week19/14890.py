import sys
input = sys.stdin.readline

def check_line(line):
	visited = [0] * n # 경사로 체크
	
	for i in range(1, n):
		# 높이 차이 1이 아니면 불가능
		if abs(line[i - 1] - line[i]) > 1:
			return False
		
		# 내리막길
		if line[i - 1] - line[i] == 1:
			for j in range(l): # (i) ~ (i + (l - 1))
				# 범위 밖, 높이 다를 때, 이미 경사로 존재
				if i + j >= n or line[i] != line[i + j] or visited[i + j]:
					return False
				visited[i + j] = 1
				
		# 오르막길
		elif line[i - 1] - line[i] == -1:
			for j in range(l): # (i - 1) ~ (i - 1 - (l - 1))
				# 범위 밖, 높이 다를 때, 이미 경사로 존재
				if i - 1 - j < 0 or line[i - 1] != line[i - 1 - j] or visited[i - 1 - j]:
					return False
				visited[i - 1 - j] = 1
	
	return True
	
n, l = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)] # 이차원 배열
answer = 0 # 답

for a in array:
	if check_line(a):
		answer += 1

for j in range(n):
	if check_line([array[i][j] for i in range(n)]):
		answer += 1

print(answer)