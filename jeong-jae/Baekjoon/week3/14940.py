import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b, n, m, array):
    distances = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((a, b))
    distances[a][b] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 1 and distances[nx][ny] == -1:
                q.append((nx, ny))
                distances[nx][ny] = distances[x][y] + 1

    return distances

def solution(n, m, array):
    a, b = -1, -1
    for i in range(n): # 목표 지점 찾기
        for j in range(m):
            if array[i][j] == 2:
                a, b = i, j
                break
        if a != -1:
            break
    
    distances = bfs(a, b, n, m, array)

    for i in range(n):
        for j in range(m):
            if array[i][j] == 0: # 0
                print(0, end=' ')
            else: # 1, 2
                print(distances[i][j], end=' ')
        print()

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
solution(n, m, array)

'''
초기: 각 지점에서 목표지점까지 BFS 수행 -> 시간복잡도 너무 커짐
해결: 목표 지점을 출발 지점으로 하여 각 지점까지 BFS로 거리 저장 -> 시간복잡도 효율적
'''