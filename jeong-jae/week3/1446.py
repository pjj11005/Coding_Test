import sys
import heapq
input = sys.stdin.readline

def solution(n, d, graph):
    distance = [int(1e9)] * (10001)
    distance[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 갱신된적 있음
            continue
        for i in graph[now]: # 다음으로 갈 지역 추가
            cost = i[1] + dist
            if i[0] <= d and cost < distance[i[0]]: # 갱신 가능
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[d]
        
n, d = map(int, input().split())
graph = [[(i + 1, 1)] for i in range(10001)] # 다음 위치까지 거리는 1(무조건 하나씩 넣어줘야 다음 지점으로 이동 가능)
for i in range(n):
    s, e, dist = map(int, input().split())
    graph[s].append((e, dist))
print(solution(n, d, graph))

'''
제공되는 지름길의 양 끝점의 위치가 해당 목적지보다 클 때를 대비하여 최대 범위로 graph와 distance 지정 필요
'''