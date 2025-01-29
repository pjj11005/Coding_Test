import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    if n < 100:  # 한자리, 두자리
        print(n)
    else:  # 세자리 or 1000
        answer = 99  # 두자리까지 개수 더함

        # n까지 개수 계산
        for num in range(100, int(n) + 1):
            # 등차수열 계산
            num = str(num)
            if (2 * int(num[1])) == int(num[0]) + int(num[2]):
                answer += 1
        print(answer)


if __name__ == "__main__":
    solution()
