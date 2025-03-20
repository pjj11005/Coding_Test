import sys
from collections import deque

input = sys.stdin.readline


def bfs(s1, s2, s3):
    q = deque([(s1, s2, s3, 0)])
    visited = {s1 + "/" + s2 + "/" + s3}

    while q:
        a, b, c, count = q.popleft()

        # 목표 상태에 도달한 경우
        if a == "A" * len(a) and b == "B" * len(b) and c == "C" * len(c):
            return count

        # 다음 가능한 상태 생성
        states = []
        if a:
            states.append((a[:-1], b + a[-1], c, count + 1))
            states.append((a[:-1], b, c + a[-1], count + 1))
        if b:
            states.append((a + b[-1], b[:-1], c, count + 1))
            states.append((a, b[:-1], c + b[-1], count + 1))
        if c:
            states.append((a + c[-1], b, c[:-1], count + 1))
            states.append((a, b + c[-1], c[:-1], count + 1))

        # 방문하지 않은 상태에 대해서만 큐에 추가
        for state in states:
            s = "/".join(state[:3])
            if s not in visited:
                visited.add(s)
                q.append(state)

    return -1


def solution():
    a = input().split()
    b = input().split()
    c = input().split()

    s1 = a[1] if a[0] != "0" else ""
    s2 = b[1] if b[0] != "0" else ""
    s3 = c[1] if c[0] != "0" else ""

    print(bfs(s1, s2, s3))


if __name__ == "__main__":
    solution()
