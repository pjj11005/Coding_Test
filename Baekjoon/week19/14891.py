import sys
from collections import deque
input = sys.stdin.readline

def rotate_gear(gear_num, direct):
	left = [chain[i][2] for i in range(3)] # 왼쪽 톱니바퀴 2번 인덱스
	right = [chain[i][6] for i in range(1, 4)] # 오른쪽 톱니바퀴 6번 인덱스
	chain[gear_num].rotate(direct) # 회전
	
	# gear_num 톱니바퀴의 왼쪽 회전
	temp_dir = direct
	for i in range(gear_num -1, -1, -1):
		if left[i] != right[i]:
			temp_dir *= -1
			chain[i].rotate(temp_dir)
		else:
			break
	
	# gear_num 톱니바퀴의 오른쪽 회전
	temp_dir = direct
	for i in range(gear_num + 1, 4):
		if left[i - 1] != right[i - 1]: # 3개씩이라 -1 해줌
			temp_dir *= -1
			chain[i].rotate(temp_dir)
		else:
			break
	
def score(chain):
	answer = 0
	
	for i in range(4):
		if chain[i][0] == 1:
			answer += (1 << i)
			
	return answer
	
chain = [deque(list(map(int, input().strip()))) for _ in range(4)]

for _ in range(int(input())):
	num, direct = map(int, input().split())
	rotate_gear(num - 1, direct) # 톱니바퀴 방향 구하기

print(score(chain))


''' bfs(내 풀이)
import sys
from collections import deque
input = sys.stdin.readline

def bfs(num, direct, chain):
	visited = [0] * 5 # 방문
	direction = [0] * 5 # 각 톱니바퀴 방향
	direction[num] = direct
	visited[num] = 1
	q = deque([num])
	
	while q:
		now = q.popleft()
		
		for i in graph[now]: # 방향 지정
			if not visited[i]:
				visited[i] = 1
				if i < now:
					if chain[i][2] != chain[now][6]:
						direction[i] = -direction[now]
				else:
					if chain[i][6] != chain[now][2]:
						direction[i] = -direction[now]
				
				if direction[i] != 0: # 회전 가능
					q.append(i)
	
	return direction

def solution(chain):
	answer = 0
	
	for i in range(1, 5):
		if chain[i][0] == 1:
			answer += (2**(i - 1))
			
	return answer
	
chain = [[]] + [list(map(int, input().strip())) for _ in range(4)]
graph = [[], [2], [1, 3], [2, 4], [3]]

for _ in range(int(input())):
	num, direct = map(int, input().split())
	direction = bfs(num, direct, chain) # 톱니바퀴 방향 구하기
	
	# 방향에 따라 회전 시키기
	for i in range(1, 5):
		if direction[i] != 0:
			temp = deque(chain[i])
			temp.rotate(direction[i])
			chain[i] = list(temp)

print(solution(chain))
'''