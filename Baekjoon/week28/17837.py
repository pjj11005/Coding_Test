import sys

input = sys.stdin.readline


def move_horse(i, n, array, direct, horses, groups):
    x, y, d = horses[i]
    dx, dy = direct[d]
    
    # 다음 위치
    nx, ny = x + dx, y + dy
    
    # 파란색이나 범위 밖
    if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
        # 방향 반대로 전환
        d = d + 1 if d % 2 == 0 else d - 1
        horses[i][2] = d # 방향 변환 정보 저장
        dx, dy = direct[d]
        nx, ny = x + dx, y + dy
        
        # 반대 방향도 파란색이나 범위 밖이면 안됨
        if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] == 2:
            return False
    
    # 현재 말 부터 위에 있는 모든 말들 이동
    idx = groups[x][y].index(i) # 현재 말의 위치
    moving = groups[x][y][idx:] # 현재 말부터 위의 모든 말
    groups[x][y] = groups[x][y][:idx] # 원래 위치에서 제거
    
    # 빨간색이면 뒤집기
    if array[nx][ny] == 1:
        moving = moving[::-1]
    
    # 말들을 새로운 위치로 이동 -> 이 부분을 빼먹었다...
    for horse in moving:
        groups[nx][ny].append(horse)
        horses[horse][0], horses[horse][1] = nx, ny # 말들의 위치 업데이트
    
    # 4개 이상 쌓였는지 확인 -> 새로 쌓인 곳의 개수만 보면 된다
    return len(groups[nx][ny]) >= 4
        
def solution():
    n, k = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    direct = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 우, 좌, 상, 하
    horses = []
    groups = [[[] for _ in range(n)] for _ in range(n)]
    
    # 말의 정보, 그룹 정보 생성
    for i in range(k):
        x, y, d = map(lambda x: int(x) - 1, input().split())
        horses.append([x, y, d])
        groups[x][y].append(i)
    
    
    turn = 1
    while turn <= 1000:
        # 모든 말에 대해 순서대로 이동
        for i in range(k):
            if move_horse(i, n, array, direct, horses, groups):
                print(turn)
                exit(0)
        turn += 1
    
    print(-1)
    
if __name__ == '__main__':
    solution()
