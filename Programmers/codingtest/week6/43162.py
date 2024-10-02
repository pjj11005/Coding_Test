from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)
                
    i = 0         
    while i < n:
        if not visited[i]:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                now = q.popleft()
                for j in graph[now]:
                    if not visited[j]:
                        visited[j] = 1
                        q.append(j)
            answer += 1
        i += 1 
        
    return answer