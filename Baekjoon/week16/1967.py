import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs 탐색
def dfs(start, weight):
    for next_node, next_weight in graph[start]:
        if distance[next_node] == -1: # 도달 X
            distance[next_node] = weight + next_weight
            dfs(next_node, weight + next_weight)
            
n = int(input())
graph = [[] for _ in range(n + 1)]
# 간선 및 가중치 저장
for i in range(n - 1):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

# 루트에서 가장 먼 노드 구하기
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
max_node = distance.index(max(distance))

# 가장 먼 노드에서 가장 먼 길이 찾기
distance = [-1] * (n + 1)
distance[max_node] = 0
dfs(max_node, 0)
print(max(distance))