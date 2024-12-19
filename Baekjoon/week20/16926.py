import sys
from collections import deque

input = sys.stdin.readline


# 이차원 배열 값들 deque로 변환하는 함수
def array_to_deque(array):
    transformed = []
    x1, y1, x2, y2 = 0, 0, n - 1, m - 1

    for _ in range(min(n, m) // 2):
        q = deque()

        for i in range(y1, y2):  # 상
            q.append(array[x1][i])

        for i in range(x1, x2):  # 우
            q.append(array[i][y2])

        for i in range(y2, y1, -1):  # 하
            q.append(array[x2][i])

        for i in range(x2, x1, -1):  # 좌
            q.append(array[i][y1])

        transformed.append(q)
        x1, y1, x2, y2 = x1 + 1, y1 + 1, x2 - 1, y2 - 1

    return transformed


# 회전 함수
def rotation(transformed, r):
    for t in transformed:
        t.rotate(-(r % len(t)))

    return transformed


# deque들 이차원 배열로 변환하는 함수
def deque_to_array(transformed):
    array = [[0] * m for _ in range(n)]
    x1, y1, x2, y2 = 0, 0, n - 1, m - 1

    for t in transformed:

        for i in range(y1, y2):  # 상
            x = t.popleft()
            array[x1][i] = x

        for i in range(x1, x2):  # 우
            x = t.popleft()
            array[i][y2] = x

        for i in range(y2, y1, -1):  # 하
            x = t.popleft()
            array[x2][i] = x

        for i in range(x2, x1, -1):  # 좌
            x = t.popleft()
            array[i][y1] = x

        x1, y1, x2, y2 = x1 + 1, y1 + 1, x2 - 1, y2 - 1

    return array


n, m, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

transformed = array_to_deque(array)  # 이차원 배열 -> deque들로 변환
rotation(transformed, r)  # r바퀴 회전
array = deque_to_array(transformed)  # deque들 -> 이차원 배열로 변환환

for a in array:
    print(*a)
