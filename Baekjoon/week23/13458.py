import sys

input = sys.stdin.readline


def min_count(n, b, c, array):
    count = 0
    for a in array:
        # 총감독 1명 배치 후 나머지 있을 때
        if a > b:
            a -= b
            # 부감독
            if a % c == 0:  # 나누어 떨어짐
                count += a // c
            else:
                count += (a // c) + 1

        count += 1  # 총감독 수 증가

    return count


def solution():
    n = int(input())
    array = list(map(int, input().split()))
    b, c = map(int, input().split())
    print(min_count(n, b, c, array))


if __name__ == "__main__":
    solution()
