import sys

input = sys.stdin.readline

def dfs(horse, cnt, total):
    global answer
    if cnt == 10: # 모든 턴 종료
        answer = max(answer, total)
        return

    # 각각의 경우 이동
    for i in range(4):
        current = horse[i]
        if current == 32: # 도착한 말 제외
            continue
            
        # 다음 위치 계산
        move_count = dice[cnt]
        next_position = current
        
        # 파란색 칸에서 시작
        if next_position in [5, 10, 15]: # 10, 20, 30에 해당하는 인덱스
            next_position = next_pos[next_position][1]
            move_count -= 1
        
        # 남은 이동 수행
        for _ in range(move_count):
            if next_position == 32: # 도착 지점
                break
            next_position = next_pos[next_position][0]
        
        # 도착 지점은 아닌데 다른 말 위에 도착
        if next_position != 32 and next_position in horse:
            continue
        
        # 백트래킹
        prev = horse[i]
        horse[i] = next_position
        dfs(horse, cnt + 1, total + score[next_position])
        horse[i] = prev

dice = list(map(int, input().split()))

# 윷놀이 판의 점수 (인덱스가 위치를 나타냄)
score = [
    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, # 0 ~ 10
    22, 24, 26, 28, 30, 32, 34, 36, 38, 40, # 11 ~ 20
    13, 16, 19, 25, 22, 24, # 21 ~ 26 (10, 20에서 시작하는 파란색 경로)
    28, 27, 26,  # 27 ~ 29 (30에서 시작하는 파란색 경로)
    30, 35, 0 # 마지막 부분
]

# 다음 위치로 이동하는 경로 : 이게 핵심
next_pos = [
    [1], [2], [3], [4], [5],          # 0~4
    [6, 21], [7], [8], [9], [10],     # 5~9
    [11, 25], [12], [13], [14], [15], # 10~14
    [16, 27], [17], [18], [19], [20], # 15~19
    [32], [22], [23], [24], [30],     # 20~24
    [26], [24], [28], [29], [24],     # 25~29
    [31], [20], [32]      # 30~32
]
answer = 0 # 답
horse = [0, 0, 0, 0] # 말 4개의 초기 위치
dfs(horse, 0, 0)
print(answer)
