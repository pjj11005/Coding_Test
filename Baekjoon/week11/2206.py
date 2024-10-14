import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, array):
    answer = -1
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 벽을 부순 경우와 부수지 않은 경우를 위해 3차원
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    visited[0][0][0] = 1
    q.append((0, 0, 0, 1)) # x, y, broken(벽 부수기), dist(거리)
    
    while q:
        x, y, broken, dist = q.popleft()
        if x == n - 1 and y == m - 1:
            return dist
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if array[nx][ny] == 0 and not visited[nx][ny][broken]: # 빈칸
                    visited[nx][ny][broken] = 1
                    q.append((nx, ny, broken, dist + 1))
                elif array[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]: # 벽 뚫기
                    visited[nx][ny][1] = 1
                    q.append((nx, ny, 1, dist + 1))

    return answer
    
n, m = map(int, input().split())
array = [list(map(int, input().strip())) for _ in range(n)]
print(solution(n, m , array))