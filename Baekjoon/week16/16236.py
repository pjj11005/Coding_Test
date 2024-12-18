import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, length):
    dist = [[-1] * n for _ in range(n)] # 거리 및 방문 처리
    q = deque([(x, y)])
    dist[x][y] = 0
    fishes = [] # 잡아먹을 수 있는 물고기들
    
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1,0), (0,-1), (0,1), (1,0)):
            nx, ny = x + dx, y + dy
            # 이동 가능
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                if array[nx][ny] <= length:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if 0 < array[nx][ny] < length:
                        fishes.append((dist[nx][ny], nx, ny))
    return sorted(fishes) if fishes else []
    
def solution(n, array):
    answer = 0 # 물고기 잡아먹는 시간
    count = 0 # 잡아먹은 물고기 수
    length = 2 # 아기 상어의 크기
    
    # 초기 아기 상어 위치
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if array[i][j] == 9:
                x, y = i, j
                array[i][j] = 0
                
    while True:
        # 먹을 수 있는 물고기 정보 저장
        fishes = bfs(x, y, length)
        
        # 종료
        if not fishes:
            return answer
            
        # 물고기 잡아 먹기
        dist, a, b = fishes[0] # 먹을 물고기 정보
        
        # 아기 상어 이동
        answer += dist
        array[a][b] = 0
        count += 1
        
        # 몸집 증가
        if length == count:
            length += 1
            count = 0
            
        x, y = a, b
            
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, array))