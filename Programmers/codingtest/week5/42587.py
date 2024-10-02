from collections import deque

def solution(priorities, location):
    answer = 0
    count = 0
    q = deque()
    for i, p in enumerate(priorities):
        q.append((i, p))
    while q:
        flag = True
        i, p = q.popleft()
        for _, p2 in list(q):
            if p < p2:
                flag = False
                break
        if flag:  # 제거 가능
            count += 1
            if i == location:
                answer = count
                break
        else:  # 다시 넣기
            q.append((i, p))
    return answer