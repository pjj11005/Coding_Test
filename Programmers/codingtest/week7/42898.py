def solution(m, n, puddles):
    array = [[0] * m for _ in range(n)]
    for y, x in puddles:
        array[x - 1][y - 1] = -1
    array[0][0] = 1
    for x in range(n):
        for y in range(m):
            if array[x][y] != -1: # 물 웅덩이 아닐때
                for dx, dy in [(0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and array[nx][ny] != -1:
                        array[x][y] += array[nx][ny]
    return (array[n - 1][m - 1]) % 1000000007