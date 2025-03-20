import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, x = heapq.heappop(q)

        # 이미 더 짧을 때
        if dist < distance[x]:
            continue

        # 최단 거리 진행
        for i, cost in graph[x]:
            if dist + cost < distance[i]:
                distance[i] = dist + cost
                heapq.heappush(q, (distance[i], i))

    return distance


def solution():
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, input().split())

    # 최종 거리
    d1 = dijkstra(v1, n, graph)
    d2 = dijkstra(v2, n, graph)

    answer = min(d1[1] + d1[v2] + d2[n], d2[1] + d2[v1] + d1[n])
    print(-1 if answer >= INF else answer)


if __name__ == "__main__":
    solution()
