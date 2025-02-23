import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph, distance, n):
    first = ["-"] * (n + 1)  # 각 노드로 가기 위한 첫 번째 경유지 저장
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        c, node = heapq.heappop(q)

        # 이미 더 짧은 경로 있음
        if distance[node] < c:
            continue

        # 현재 노드에서 진행 가능한 노드 탐색
        for i in graph[node]:
            cost = c + i[0]  # 새로운 비용
            if distance[i[1]] > cost:
                if node == start:  # 시작 노드에서 직접 연결
                    first[i[1]] = str(i[1])  # 첫번째 경유지가 됨
                else:  # 다른 노드 거쳐서 진행
                    first[i[1]] = str(first[node])  # 중간 지점의 첫번째 경유지를 값으로 가지게 됨
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    return first[1:]


def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))

    for i in range(1, n + 1):
        distance = [INF] * (n + 1)
        print(*dijkstra(i, graph, distance, n))


if __name__ == "__main__":
    solution()
