import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    n = int(input())

    # game[i][j] : i + 1번 이닝에서 j + 1번 선수의 결과
    game = [list(map(int, input().split())) for _ in range(n)]
    order = list(range(1, 9))  # 1번 선수(0번)은 4번이므로 제외
    result = 0

    for x in permutations(order, 8):  # 나머지 8명의 타순 생성
        x = list(x)
        batter = x[:3] + [0] + x[3:]  # 4번 타자는 1번 선수(0번)
        number, point = 0, 0  # 현재 타자 번호, 득점

        for i in range(n):  # 각 이닝
            out = 0  # 아웃 카운트
            p1 = p2 = p3 = 0  # 1, 2, 3 루 주자 유무

            while out < 3:  # 3 아웃 까지
                # 현재 타자의 결과
                g = game[i][batter[number]]
                if g == 0:  # 아웃
                    out += 1
                elif g == 1:  # 안타
                    point += p3
                    p1, p2, p3 = 1, p1, p2
                elif g == 2:  # 2루타
                    point += p2 + p3
                    p1, p2, p3 = 0, 1, p1
                elif g == 3:  # 3루타
                    point += p1 + p2 + p3
                    p1, p2, p3 = 0, 0, 1
                else:  # 홈런
                    point += p1 + p2 + p3 + 1
                    p1, p2, p3 = 0, 0, 0

                number = (number + 1) % 9  # 다음 타자

        result = max(result, point)

    print(result)


if __name__ == "__main__":
    solution()
