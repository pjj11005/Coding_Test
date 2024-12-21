import sys

input = sys.stdin.readline


# 90도 회전 시키는 함수
def rotation_90(array):
    return [list(row) for row in zip(*array[::-1])]


# 위로 밀기 함수
def move(array):
    new_array = [[0] * n for _ in range(n)]

    for i in range(n):
        pos, prev = 0, 0  # 새로 저장할 위치, 이전의 값
        for j in range(n):
            if array[i][j] == 0:  # 0이면 pass
                continue

            if prev == 0:  # 이전 숫자 없음
                prev = array[i][j]
            else:
                if prev == array[i][j]:  # 이전 숫자와 현재가 같음
                    new_array[i][pos] = prev * 2
                    pos += 1
                    prev = 0
                else:  # 이전 숫자와 현재가 다름
                    new_array[i][pos] = prev
                    pos += 1
                    prev = array[i][j]

        # 행의 처리가 끝났는데 아직 저장하지 않은 숫자가 있다면 마지막 숫자 저장
        if prev != 0:
            new_array[i][pos] = prev

    return new_array


# dfs 함수
def dfs(depth, array):
    global answer
    if depth == 5:
        answer = max(answer, max(max(a) for a in array))
        return

    for i in range(4):
        new_array = move([row[:] for row in array])
        dfs(depth + 1, new_array)
        array = rotation_90(array)


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
answer = 0  # 답

dfs(0, array)
print(answer)
