import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    indegree = [0] * (n + 1)  # 진입 차수
    graph = [[] for _ in range(n + 1)]
    answer = []

    # 진입 차수 계산
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    # 진입 차수 0인 노드 담기
    q = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    # 위상 정렬 진행
    while q:
        x = q.popleft()
        answer.append(x)

        for i in graph[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 정답 출력
    print(*answer)


if __name__ == "__main__":
    solution()
