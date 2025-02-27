from collections import deque

def solution(queue1, queue2):
    # 두 큐의 합 계산
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    
    # 합이 홀수면 불가능
    if total % 2 != 0:
        return -1
    
    # 목표값 계산
    target = total // 2
    
    # 큐 변환
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 최대 작업 횟수 제한 (두 큐 길이의 3배)
    limit = len(queue1) * 3
    count = 0
    
    # 두 큐의 합이 같아질 때까지 반복
    while count <= limit:
        if sum1 == target:
            return count
        
        if sum1 > target:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        else:
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
            
        count += 1
    
    return -1
