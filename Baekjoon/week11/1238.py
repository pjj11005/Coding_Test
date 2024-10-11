# 역방향 그래프 추가 + 출발점을 x로 두기 : python 56ms
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(graph, start):
    distance = [INF] * (n + 1) # 거리 리스트
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost: # 탐색할 필요 없음
            continue
        
        for i, time in graph[now]:
            if distance[i] > cost + time: # 거리 갱신 가능
                distance[i] = cost + time
                q.append((cost + time, i))
    
    return distance

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)] # 역방향 그래프
for i in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))
    reversed_graph[b].append((a, time))

dist1 = solution(graph, x) # x에서 모든 지점까지의 시간 : 돌아가는 시간
dist2 = solution(reversed_graph, x) # 모든 지점에서 x까지 가는 시간 : x로 가는 시간

answer = 0
for i in range(1, n + 1): # 오고 가는 최단거리 시간의 합의 최댓값 갱신
    answer = max(answer, dist1[i] + dist2[i])
print(answer)


''' 내 풀이 : python 3404ms
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(start, x):
    distance = [INF] * (n + 1) # 거리 리스트
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)

        if distance[now] < cost: # 탐색할 필요 없음
            continue
        
        for i, time in graph[now]:
            if distance[i] > cost + time: # 거리 갱신 가능
                distance[i] = cost + time
                q.append((cost + time, i))
    
    return distance[x]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, time = map(int, input().split())
    graph[a].append((b, time))

answer = 0
for start in range(1, n + 1): # 오고 가는 최단거리 시간의 합의 최댓값 갱신
    answer = max(answer, solution(start, x) + solution(x, start))
print(answer)
'''