import sys
input = sys.stdin.readline

def dfs(idx, cnt):
	global answer
	
	# m개씩 치킨집 골라서 최소 치킨 거리 구하기
	if cnt == m:
		total = 0 # 거리합
		for x, y in home:
			temp_dist = float('inf') # 특정 집에서 최소 치킨 거리
			for i, chick in enumerate(chicken):
				a, b = chick
				if visited[i]: # 선택된 치킨집
					temp_dist = min(temp_dist, abs(x - a) + abs(y - b))
			total += temp_dist
			
		answer = min(answer, total)
		return
	
	# dfs로 치킨집 선택
	for i in range(idx, len(chicken)):
		visited[i] = 1
		dfs(i + 1, cnt + 1)
		visited[i] = 0
	
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf') # 답
home, chicken = [], [] # 집, 치킨집 좌표

# 집, 치킨집 좌표 저장
for i in range(n):
	for j in range(n):
		if array[i][j] == 1: # 집
			home.append((i, j))
		elif array[i][j] == 2: # 치킨집
			chicken.append((i, j))

visited = [0] * len(chicken) # 방문
dfs(0, 0)
print(answer)

''' combiantions(내 풀이)
import sys
from itertools import combinations
input = sys.stdin.readline

def solution(n, m, array):
	answer = float('inf') # 답
	home, chicken = [], [] # 집, 치킨집 좌표
	
	# 집, 치킨집 좌표 저장
	for i in range(n):
		for j in range(n):
			if array[i][j] == 1: # 집
				home.append((i, j))
			elif array[i][j] == 2: # 치킨집
				chicken.append((i, j))
	
	# m개씩 치킨집 골라서 최소 치킨 거리 구하기
	for comb in combinations(chicken, m):
		total = 0 # 거리합
		for x, y in home:
			temp_dist = float('inf') # 특정 집에서 최소 치킨 거리
			for i, j in list(comb):
				temp_dist = min(temp_dist, abs(x - i) + abs(y - j))
			total += temp_dist
		answer = min(answer, total)
			
	return answer
	
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, array))
'''