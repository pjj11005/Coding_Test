import sys
input = sys.stdin.readline

def solution(x, y, d):
	answer = 1
	visited[x][y] = 1

	while True:
		if not visited[x][y]: # 청소 안됨
			visited[x][y] = 1
			answer += 1
		
		is_possible = False # 청소 가능 구역 유무
		for dx, dy in move:
			nx, ny = x + dx, y + dy
			if not visited[nx][ny] and array[nx][ny] == 0:
				is_possible = True
		
		if is_possible: # 청소 가능 구역 있음
			d = (d + 3) % 4 # 반시계 방향 회전
			dx, dy = move[d][0], move[d][1]
			nx, ny = x + dx, y + dy
			if not visited[nx][ny] and array[nx][ny] == 0: # 전진 가능
				x, y = nx, ny
		else: # 청소 가능 구역 없음
			dx, dy = move[d][0], move[d][1]
			dx *= -1
			dy *= -1
			nx, ny = x + dx, y + dy
			if array[nx][ny] == 0: # 후진 가능
				x, y = nx, ny
			else:
				break
			
	return answer

n, m = map(int, input().split())
r, c, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(solution(r, c, d))