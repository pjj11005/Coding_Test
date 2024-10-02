from collections import deque
def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque([(0, 0, 1)])
    visited[0][0] = 1
    while q:
        x, y, count = q.popleft()
        if x == n - 1 and y == m - 1:
            answer = count
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, count + 1))
                
    return answer