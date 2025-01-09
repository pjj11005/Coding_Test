"""코드트리 아름다운 수"""


def check(num_list, n):
    pivot = num_list[0]
    cnt = 1
    for i in range(1, n):
        if pivot != num_list[i]:
            if cnt % pivot != 0:  # 숫자 틀림
                return False
            pivot = num_list[i]
            cnt = 1
        else:
            cnt += 1

    # 마지막 체크
    if cnt % pivot != 0:  # 숫자 틀림
        return False
    return True


def dfs(num_list, n):
    global answer

    # 체크
    if len(num_list) == n:
        if check(num_list, n):
            answer += 1
        return

    # 숫자 이어 붙이기
    for i in range(1, 5):
        dfs(num_list + [i], n)


def solution():
    global answer
    n = int(input())
    answer = 0

    dfs([], n)
    print(answer)


if __name__ == "__main__":
    solution()
