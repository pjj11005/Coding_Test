from collections import deque
import sys
input = sys.stdin.readline

def check_move(array, x, y, direction):
    n = len(array)
    # 가로 방향일 때
    if direction == 1:
        if 0 <= x < n and 0 <= y-1 < n and 0 <= y+1 < n:
            if array[x][y-1] != '1' and array[x][y] != '1' and array[x][y+1] != '1':
                return True
    # 세로 방향일 때
    else:
        if 0 <= x-1 < n and 0 <= x+1 < n and 0 <= y < n:
            if array[x-1][y] != '1' and array[x][y] != '1' and array[x+1][y] != '1':
                return True
    return False

def check_rotate(array, x, y):
    n = len(array)
    # 3x3 영역 검사
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (0 <= i < n and 0 <= j < n) or array[i][j] == '1':
                return False
    return True

def bfs(n, array):
    # 초기 위치와 목표 위치 찾기
    b, e = [], []
    for i in range(n):
        for j in range(n):
            if array[i][j] == 'B':
                b.append((i, j))
            elif array[i][j] == 'E':
                e.append((i, j))
    
    # 중앙점과 방향 설정 (가로:1, 세로:0)
    start = (b[1][0], b[1][1], 1 if b[0][0] == b[1][0] else 0)
    end = (e[1][0], e[1][1], 1 if e[0][0] == e[1][0] else 0)
    
    # BFS 탐색
    visited = set([start])
    q = deque([(start[0], start[1], start[2], 0)])  # x, y, 방향, 이동횟수
    
    while q:
        x, y, direction, count = q.popleft()
        if (x, y, direction) == end:
            return count
            
        # 상하좌우 이동
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                next_state = (nx, ny, direction)
                if next_state not in visited and check_move(array, nx, ny, direction):
                    visited.add(next_state)
                    q.append((nx, ny, direction, count + 1))
        
        # 회전
        if check_rotate(array, x, y):
            next_direction = 1 - direction
            next_state = (x, y, next_direction)
            if next_state not in visited:
                visited.add(next_state)
                q.append((x, y, next_direction, count + 1))
    
    return 0

def solution():
    n = int(input())
    array = [list(input().strip()) for _ in range(n)]
    print(bfs(n, array))

if __name__ == '__main__':
    solution()
