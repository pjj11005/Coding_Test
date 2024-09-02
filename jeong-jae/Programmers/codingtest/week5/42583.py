from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    road = deque()
    total = 0
    time = 1
    while q:
        if not road:  # 비어있음
            w = q.popleft()
            road.append((w, time))
            total += w
        else:  # 있음
            if total + q[0] <= weight:  # 추가 가능
                w = q.popleft()
                road.append((w, time))
                total += w

        time += 1
        if road[0][1] == time - bridge_length:
            w, t = road.popleft()
            total -= w
    answer = time + bridge_length - 1
    return answer