import sys
from collections import deque

input = sys.stdin.readline


# dp 풀이(다른 사람 풀이): 36ms
def solution2():
    s = int(input())
    dp = [i for i in range((2 * s) + 1)]  # 해당 수를 만드는 최소 시간(더 큰 수에서 삭제하는 경우 고려)
    dp[1] = 0
    dp[0] = 1

    # 계산
    for i in range(2, (2 * s) + 1):
        cnt = 2  # 초기 복사 + 붙여 넣기 횟수
        for j in range(2 * i, (2 * s) + 1, i):
            dp[j] = min(dp[i] + cnt, dp[j])  # 복붙 횟수와 비교
            dp[j - 1] = min(dp[j] + 1, dp[j - 1])  # j + 1에서 삭제 연산한 경우와 비교
            cnt += 1  # 붙여넣기 횟수 증가

    print(dp[s])


# BFS 풀이(내 풀이): 76ms
def solution():
    s = int(input())
    q = deque([(1, 0, 0)])  # 출력, 클립보드, 시간
    visited = {(1, 0)}  # (출력, 클립보드)
    answer = 0

    while q:
        present, clipboard, time = q.popleft()
        # 최소 시간
        if present == s:
            answer = time
            break

        for i in range(3):
            next_present, next_clipboard = 0, 0
            if i == 0:  # 복사
                next_clipboard = present
                next_present = present
            elif i == 1:  # 붙여넣기
                if clipboard:  # 클립보드 채워져있음
                    next_present = present + clipboard
                    next_clipboard = clipboard
            else:  # 삭제
                if present:  # 출력된게 있으면
                    next_present = present - 1
                    next_clipboard = clipboard

            # 나온적 없는 경우
            if (next_present, next_clipboard) not in visited:
                visited.add((next_present, next_clipboard))
                q.append((next_present, next_clipboard, time + 1))

    print(answer)


if __name__ == "__main__":
    solution()
