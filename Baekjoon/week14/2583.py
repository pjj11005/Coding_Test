import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    array[i][j] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and array[nx][ny] == 0:
                cnt += 1
                array[nx][ny] = 1
                q.append((nx, ny))
    return cnt

m, n, k = map(int, input().split())
array = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 이차원 리스트에 맞게 변환
    r1, r2 = m - y2, m - y1 - 1
    c1, c2 = x1, x2 - 1
    # 직사각형 칸은 1로 채우기
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            array[i][j] = 1

count = 0
answer = []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(m):
    for j in range(n):
        if array[i][j] == 0: # 0의 넓이 및 개수 파악
            count += 1
            answer.append(bfs(i, j))
            
print(count)
answer.sort()
for a in answer:
    print(a, end=' ')