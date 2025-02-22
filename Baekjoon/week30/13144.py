import sys


input = sys.stdin.readline


def solution():
    n = int(input())
    array = list(map(int, input().split()))

    left = 0
    answer = 0
    num_set = set()  # 현재 구간에서 중복을 체크할 집합

    for right in range(n):
        while array[right] in num_set:
            num_set.remove(array[left])
            left += 1

        num_set.add(array[right])
        answer += right - left + 1  # 중복 없는 구간의 길이를 더함

    print(answer)


if __name__ == "__main__":
    solution()
