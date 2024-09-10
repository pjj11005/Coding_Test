from collections import deque

def rotate_check(n, b, p):
    # 빈칸 좌표들 좌상단에 맞춤
    min_x = min([i[0] for i in b])
    min_y = min([i[1] for i in b])
    b = [(x - min_x, y - min_y) for x, y in b]
    b.sort()
    
    # 빈칸 좌표들 좌상단에 맞춤
    min_x = min([i[0] for i in p])
    min_y = min([i[1] for i in p])
    p = [(x - min_x, y - min_y) for x, y in p]
    p.sort()
    
    if b == p: # 회전 안시켜도 같을 때
        return len(b)
    
    for i in range(3): # 회전 3번
        rotated = []
        # 90도 회전된 좌표 계산
        for x, y in p:
            new_x = y
            new_y = n - 1 - x
            rotated.append((new_x, new_y))

        min_x = min([coord[0] for coord in rotated])
        min_y = min([coord[1] for coord in rotated])
        p = [(x - min_x, y - min_y) for x, y in rotated]
        p.sort()
        
        if b == p:
            return len(b)       
    
    return 0

def bfs(x, y, n, game_board, visited):
    temp = []
    q = deque([(x, y)])
    temp.append((x, y))
    while q:
        x, y  = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (game_board[nx][ny] == 0):
                visited[nx][ny] = 1
                temp.append((nx, ny))
                q.append((nx, ny))
    return temp
                
def bfs2(x, y, n, table, visited):
    temp = []
    q = deque([(x, y)])
    temp.append((x, y))
    while q:
        x, y  = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (table[nx][ny] == 1):
                visited[nx][ny] = 1
                temp.append((nx, ny))
                q.append((nx, ny))
    return temp

def solution(game_board, table):
    answer = 0
    n = len(table)
    blank = [] # 빈칸 모양
    piece = [] # 조각 모양
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:
                visited[i][j] = 1
                temp = bfs(i, j, n, game_board, visited)
                blank.append(temp)
    
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                temp = bfs2(i, j, n, table, visited)
                piece.append(temp)
    
    check = [0] * len(piece) # 퍼즐 조각 사용 유무 체크
    for b in blank:
        for i, p in enumerate(piece):
            if not check[i]:
                num = rotate_check(n, b, p)
                if num > 0:
                    check[i] = 1
                    answer += num
                    break
    return answer