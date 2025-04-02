import sys

input = sys.stdin.readline

# 방향 반전 딕셔너리로 변경 (함수 호출 제거)
REVERSE_DIRECTION = {1: 2, 2: 1, 3: 4, 4: 3}

# 방향별 이동 벡터 상수화
MOVES = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


def play_chess(n, k, board, pieces, horses):
    turn = 1
    while turn <= 1000:
        for idx in range(k):
            horse = horses[idx]
            horse_num, r, c, d = horse

            # 가장 아래 말이 아니면 이동 불가
            if pieces[r][c][0] != horse_num:
                continue

            # 다음 위치 계산
            move = MOVES[d]
            nr, nc = r + move[0], c + move[1]

            # 파란색 or 범위 밖
            if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] == 2:
                # 방향 반전
                new_direction = REVERSE_DIRECTION[d]
                horse[3] = new_direction

                # 반전 후 다음 위치
                move = MOVES[new_direction]
                nr, nc = r + move[0], c + move[1]

                # 또 파란색 or 범위 밖
                if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc] == 2:
                    continue

            # 현재 위치의 모든 말 (현재 말부터 위에 있는 모든 말)
            current_stack = pieces[r][c]
            start_idx = current_stack.index(horse_num)
            moving_pieces = current_stack[start_idx:]

            # 빨간색이면 뒤집기
            if board[nr][nc] == 1:
                moving_pieces.reverse()

            # 이동 위치의 기존 말 + 이동할 말들
            dest_stack = pieces[nr][nc]
            dest_stack.extend(moving_pieces)

            # 원래 위치 업데이트
            pieces[r][c] = current_stack[:start_idx]

            # 말 위치 정보 한번에 업데이트
            for p in moving_pieces:
                horse_idx = p - 1
                horses[horse_idx][1] = nr
                horses[horse_idx][2] = nc

            # 말이 4개 이상인지 확인
            if len(dest_stack) >= 4:
                return turn

        turn += 1

    return -1


def solution():
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 말 위치 기록
    pieces = [[[] for _ in range(n)] for _ in range(n)]

    # 말 정보 저장 (번호, 위치, 방향)
    horses = []
    for i in range(1, k + 1):
        r, c, d = map(int, input().split())
        horses.append([i, r - 1, c - 1, d])
        pieces[r - 1][c - 1].append(i)

    print(play_chess(n, k, board, pieces, horses))


if __name__ == "__main__":
    solution()
