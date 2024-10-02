from collections import deque
def solution(n, edge):
    answer = 0
    # 거리
    distance = [int(1e9)] * (n + 1)
    distance[1] = 0
    # 방문
    visited = [0] * (n + 1)
    # 각 간선 저장
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 노드까지의 최단거리 계산
    q = deque()
    q.append((1, 0))
    visited[1] = 1
    while q:
        now, dist = q.popleft()
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            if not visited[i] and dist + 1 < distance[i]:
                distance[i] = dist + 1
                visited[i] = 1
                q.append((i, dist + 1))
    
    # 가장 멀리 떨어진 노드 개수 카운드
    maximum = max(distance[1:])
    answer = distance[1:].count(maximum)
    return answer