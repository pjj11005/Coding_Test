import sys
import heapq
input = sys.stdin.readline

def solution():
    n = int(input())
    events = []
    
    for _ in range(n):
        l, h, r = map(int, input().split())
        events.append((l, -h, r)) # 시작점 : 높이 음수로 저장(큰 값부터)
        events.append((r, 0, 0))  # 끝점 : 높이 0으로 저장(끝났다는 것을 보여줌)
    
    # 이벤트 x좌표 기준으로 정렬(같은 좌표일 경우 높이 순)
    events.sort()

    result = []
    heap = [(0, float('inf'))] # (높이, 끝나는 위치)
    current_height = 0 # 현재 최고 높이

    for x, neg_h, r in events:
        # 새로운 시작점 추가
        if neg_h != 0:
            heapq.heappush(heap, (neg_h, r))

        # 끝점은 제거(끝난 건물들 힙에서 제거)
        while heap[0][1] <= x:
            heapq.heappop(heap)

        # 현재 최고 높이
        max_height = -heap[0][0]

        # 스카이라인 변화 있으면 결과에 추가
        if current_height != max_height:
            result.append((x, max_height))
            current_height = max_height
    
    return result
    
for x, h in solution():
    print(x, h, end=' ')