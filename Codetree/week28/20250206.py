import sys
from collections import deque

input = sys.stdin.readline

# 공격 경로 탐색 (BFS)
def find_attack_path(x, y, tx, ty, n, m, grid):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
    visited = [[False] * m for _ in range(n)]
    q = deque([(x, y, [])])
    visited[x][y] = True
    
    while q:
        cx, cy, path = q.popleft()
        if (cx, cy) == (tx, ty):
            return path + [(cx, cy)]
        for dx, dy in move:
            nx, ny = (cx + dx) % n, (cy + dy) % m
            if not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny, path + [(cx, cy)]))
    return None  # 경로 없음

def solution():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    time = [[0]*m for _ in range(n)]  # 마지막 공격 시간
    
    active_turrets = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                active_turrets.append((i, j))
    
    for turn in range(1, k+1):
        if len(active_turrets) <= 1:
            break
        
        # 1. 공격자 & 타겟 선정
        attacker = sorted(active_turrets, 
            key=lambda x: (grid[x[0]][x[1]], -time[x[0]][x[1]], -(x[0]+x[1]), -x[1]))[0]
        target = sorted(active_turrets, 
            key=lambda x: (-grid[x[0]][x[1]], time[x[0]][x[1]], (x[0]+x[1]), x[1]))[0]
        
        ax, ay = attacker
        tx, ty = target
        
        # 2. 공격자 강화
        grid[ax][ay] += (n + m)
        time[ax][ay] = turn
        damage = grid[ax][ay]
        
        # 3. 레이저 공격 시도
        attack_path = find_attack_path(ax, ay, tx, ty, n, m, grid)
        affected = set([(ax, ay), (tx, ty)])
        
        if attack_path:
            for x, y in attack_path[1:-1]:  # 경로 상의 포탑들
                grid[x][y] -= damage // 2
                affected.add((x, y))
            grid[tx][ty] -= damage
        else:
            # 4. 포탄 공격
            bomb_dir = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
            grid[tx][ty] -= damage
            for dx, dy in bomb_dir:
                nx, ny = (tx + dx) % n, (ty + dy) % m
                if grid[nx][ny] > 0 and (nx, ny) != (ax, ay):
                    grid[nx][ny] -= damage // 2
                    affected.add((nx, ny))
        
        # 5. 포탑 재정비
        active_turrets = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    if (i, j) not in affected:
                        grid[i][j] += 1
                    active_turrets.append((i, j))
    
    print(max(map(max, grid)) if active_turrets else 0)

if __name__ == "__main__":
    solution()
