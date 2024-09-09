from collections import deque

def check(mx, my, rectangle):
    flag1 = False # 제대로 직사각형 위를 지나는지
    flag2 = False # 다른 직사각형 안쪽 유무 체크
    for x1, y1, x2, y2 in rectangle:
        if (x1 <= mx <= x2 and (my == y1 or my == y2)) or (y1 <= my <= y2 and (mx == x1 or mx == x2)):
            flag1 = True
        if x1 < mx < x2 and y1 < my < y2:
            flag2 = True
            
    if flag1 == True and flag2 == False:
        return True
    else:
        return False
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    visited = [[0]*51 for _ in range(51)]
    q = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = 1
    while q:
        x, y, dist = q.popleft()
        if x == itemX and y == itemY:
            answer = dist
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            mx, my = (nx + x) / 2, (ny + y) / 2
            if check(mx, my, rectangle) and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, dist + 1))
    return answer