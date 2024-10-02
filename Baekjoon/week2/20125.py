import sys
input = sys.stdin.readline

def solution(n, array):
    x, y = 0, 0
    answer = []
    for i in range(n): # 심장 찾기
        for j in range(n):
            if array[i][j] == '*':
                x, y = i + 1, j
                print(x + 1, y + 1)
                break
        if x != 0 and y != 0:
            break

    a, b = x, y # 찾는 좌표
    count = 0
    while b > 0: # 왼팔
        b -= 1
        if array[a][b] == '_':
            break
        count += 1
    answer.append(count)
    b = y
    count = 0

    while b < n - 1:  # 오른팔
        b += 1
        if array[a][b] == '_':
            break
        count += 1
    answer.append(count)
    b = y
    count = 0

    while a < n - 1:  # 허리
        a += 1
        if array[a][b] == '_':
            break
        count += 1
    answer.append(count)
    x = a - 1
    a -= 1
    b = y - 1
    count = 0

    while a < n - 1:  # 왼다리
        a += 1
        if array[a][b] == '_':
            break
        count += 1
    answer.append(count)
    a = x
    b = y + 1
    count = 0

    while a < n - 1:  # 오른다리
        a += 1
        if array[a][b] == '_':
            break
        count += 1
    answer.append(count)

    for a in answer:
        print(a, end = ' ')

n = int(input())
array = [list(input()) for _ in range(n)]
solution(n, array)