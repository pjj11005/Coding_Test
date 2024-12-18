import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs로 독립집합 크기 계산
def dfs(node):
    visited[node] = True
    dp[node][1] = weights[node] # 현재 노드 포함
    dp[node][0] = 0 # 현재 노드 미포함

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            # 현재 노드 포함 -> 자식 노드 미포함
            dp[node][1] += dp[next_node][0]
            # 현재 노드 미포함 -> 자식 노드 포함 or 미포함 중 max
            dp[node][0] += max(dp[next_node][0], dp[next_node][1])

# 독립 집합 구성 추적
def trace(node, state):
    visited[node] = True

    # 현재 노드 포함
    if state:
        result.append(node)
        # 자식 미포함
        for next_node in graph[node]:
            if not visited[next_node]:
                trace(next_node, 0)
    # 현재 노드 미포함
    else:
        # 자식 노드들은 dp값이 더 큰 것 선택
        for next_node in graph[node]:
            if not visited[next_node]:
                if dp[next_node][1] > dp[next_node][0]:
                    trace(next_node, 1)
                else:
                    trace(next_node, 0)
    
n = int(input())
weights = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(n + 1)] # [미포함, 포함]
visited = [False] * (n + 1)

# 독립집합 크기 계산
dfs(1)

# 독립 집합 구성 추적
result = []
visited = [False] * (n + 1)
if dp[1][1] > dp[1][0]:
    trace(1, 1)
else:
    trace(1, 0)

print(max(dp[1][0], dp[1][1]))
print(*sorted(result))