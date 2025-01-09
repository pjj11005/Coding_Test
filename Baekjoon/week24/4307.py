import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    for _ in range(n):
        l, m = map(int, input().split())  # 막대 길이, 개미의 수
        ants = [int(input()) for _ in range(m)]  # 개미들의 위치

        min_time = 0
        max_time = 0

        for ant in ants:
            # 최소 시간은 가장 가까운 끝점까지의 거리
            min_time = max(min_time, min(ant, l - ant))
            # 최대 시간은 가장 먼 끝점까지의 거리
            max_time = max(max_time, max(ant, l - ant))

        print(min_time)
        print(max_time)


if __name__ == "__main__":
    solution()
