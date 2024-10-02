import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, index, union):
    # 연합 국가 좌표 리스트
    united = []
    united.append((x, y))
    union[x][y] = index
    total = array[x][y] # 총합
    count = 1 # 국가 수
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1 and (l <= abs(array[x][y] - array[nx][ny]) <= r):
                united.append((nx, ny))
                total += array[nx][ny]
                count += 1
                union[nx][ny] = index
                q.append((nx, ny))
    
    avg = total // count
    for i, j in united:
        array[i][j] = avg
                
def solution(n, l, r, array):
    answer = 0
    while True:
        union = [[-1] * n for _ in range(n)] # 연합 표시 리스트
        index = 0
        for i in range(n):
            for j in range(n):
                if union[i][j] == -1:
                    bfs(i, j, index, union)
                    index += 1
                            
        # 진행 가능 여부
        if index == n * n:
            break
        answer += 1
        
    return answer

n, l, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, l, r, array))