import sys
input = sys.stdin.readline

# 미리 계산된 모래 비율과 방향
SAND_INFO = {
    0: [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), # 좌
        (2, 0, 0.02), (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)],
    1: [(-1, -1, 0.01), (-1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), # 하
        (0, 2, 0.02), (1, -1, 0.1), (1, 1, 0.1), (2, 0, 0.05)],
    2: [(-1, -1, 0.01), (1, -1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), # 우
        (2, 0, 0.02), (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)],
    3: [(1, -1, 0.01), (1, 1, 0.01), (0, -1, 0.07), (0, 1, 0.07), (0, -2, 0.02), # 상
        (0, 2, 0.02), (-1, -1, 0.1), (-1, 1, 0.1), (-2, 0, 0.05)]
}

def spread_sand(x, y, d, arr, n):
    out_sand = 0
    sand_amount = arr[x][y]
    if sand_amount == 0:
        return 0
    
    moved_sand = 0
    arr[x][y] = 0
    
    # 미리 계산된 방향으로 모래 분배
    for dx, dy, ratio in SAND_INFO[d]:
        nx, ny = x + dx, y + dy
        sand = int(sand_amount * ratio)
        moved_sand += sand
        
        if 0 <= nx < n and 0 <= ny < n:
            arr[nx][ny] += sand
        else:
            out_sand += sand
    
    # 알파 계산
    nx, ny = x + [0, 1, 0, -1][d], y + [-1, 0, 1, 0][d]
    alpha = sand_amount - moved_sand
    if 0 <= nx < n and 0 <= ny < n:
        arr[nx][ny] += alpha
    else:
        out_sand += alpha
        
    return out_sand

def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    
    # 토네이도 이동 경로 최적화
    x = y = n // 2
    direction = 0
    move_count = 0
    max_move = 1
    
    for _ in range(n * 2 - 1):
        for _ in range(max_move):
            x += [0, 1, 0, -1][direction]
            y += [-1, 0, 1, 0][direction]
            if not (0 <= x < n and 0 <= y < n):
                print(result)
                return
            result += spread_sand(x, y, direction, arr, n)
        
        move_count += 1
        direction = (direction + 1) % 4
        if move_count == 2:
            move_count = 0
            max_move += 1

if __name__ == "__main__":
    solution()