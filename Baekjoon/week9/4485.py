import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(x, y):
    q = []    
    heapq.heappush(q, (distance[x][y], x, y))
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if dist + array[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + array[nx][ny]
                    heapq.heappush(q, (dist + array[nx][ny], nx, ny))
    
i = 1
while True:
    n = int(input())
    if n == 0:
        break
    array = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    distance[0][0] = array[0][0]
    visited[0][0] = 1
    
    solution(0, 0)
    
    print(f'Problem {i}: {distance[n - 1][n - 1]}')
    i += 1