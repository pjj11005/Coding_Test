import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(n, graph, mid, k):
    distance = [INF] * (n + 1)
    distance[1] = 0
    q = [(0, 1)]  # 비용, 노드

    while q:
        cost, node = heapq.heappop(q)

        if distance[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            # mid보다 큰 비용은 1, 작은 비용은 0으로 처리
            new_cost = cost + (1 if next_cost > mid else 0)

            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    # n번 노드까지의 비용이 k인지 확인
    return distance[n] <= k


def solution():
    global answer
    n, p, k = map(int, input().split())
    graph = defaultdict(list)

    # 최대 비용 저장
    max_cost = 0

    # 그래프 저장
    for _ in range(p):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        max_cost = max(max_cost, c)

    # 이분 탐색
    start, end = 0, max_cost
    answer = -1

    while start <= end:
        mid = (start + end) // 2
        if dijkstra(n, graph, mid, k):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    print(answer)


if __name__ == '__main__':
    solution()
