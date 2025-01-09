"""코드트리 K중에 1개를 N번 선택하기"""


def dfs(num_list, K, N):
    if len(num_list) == N:
        print(*num_list)
        return

    for i in range(1, K + 1):
        dfs(num_list + [i], K, N)

    return


def solution():
    K, N = map(int, input().split())
    dfs([], K, N)


if __name__ == "__main__":
    solution()
