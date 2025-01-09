"""코드트리 겹치지 않게 선분 그리기"""


def find_max_lines(n, array):
    dp = [1] * n

    # 안겹치는 최대 선분 찾기
    for i in range(1, n):
        for j in range(i):
            # 자신 이전의 선분과 겹치지 않으면
            if array[i][0] > array[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def solution():
    n = int(input())
    array = []

    for _ in range(n):
        a, b = map(int, input().split())
        array.append((a, b))

    array.sort()  # 오름차순
    print(find_max_lines(n, array))


if __name__ == "__main__":
    solution()
