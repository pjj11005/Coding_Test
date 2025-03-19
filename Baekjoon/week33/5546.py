import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    days = [0] * (n + 1)

    # 정해진 파스타 입력
    for _ in range(k):
        a, b = map(int, input().split())
        days[a] = b

    # dp[날짜][오늘 먹은 소스][연속 일수] : 연속 일수 -> 0은 연속 없음, 1은 연속 2일
    dp = [[[0] * 2 for _ in range(4)] for _ in range(n + 1)]

    # 첫날 초기화
    if days[1] == 0:  # 첫날 X
        for i in range(1, 4):
            dp[1][i][0] = 1
    else:  # 첫날 O
        dp[1][days[1]][0] = 1

    # 둘째 날부터 계산
    for i in range(2, n + 1):
        if days[i] == 0:  # 정해지지 X
            for j in range(1, 4):  # 오늘 선택할 소스
                for k in range(1, 4):  # 어제 먹은 소스
                    if j == k:  # 같은 소스 먹는 경우
                        dp[i][j][1] = (dp[i][j][1] + dp[i - 1][k][0]) % 10000
                    else:  # 다른 소스 먹을 때
                        dp[i][j][0] = (dp[i][j][0] + dp[i - 1][k][0] + dp[i - 1][k][1]) % 10000
        else:  # 파스타 정해진 경우
            j = days[i]
            for k in range(1, 4):  # 어제 먹은 소스
                if j == k:  # 같은 소스 먹는 경우
                    dp[i][j][1] = (dp[i][j][1] + dp[i - 1][k][0]) % 10000
                else:  # 다른 소스 먹을 때
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][k][0] + dp[i - 1][k][1]) % 10000

    # 마지막 날의 모든 경우의 수 합산
    result = 0
    for i in range(1, 4):
        for j in range(2):
            result = (result + dp[n][i][j]) % 10000

    print(result)


if __name__ == "__main__":
    solution()
