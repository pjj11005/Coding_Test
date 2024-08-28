from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    q = deque()
    for i in range(n):  # 남은 일수 저장
        day = 0
        rest = 100 - progresses[i]
        if rest % speeds[i] == 0:
            day = rest // speeds[i]
        else:
            day = (rest // speeds[i]) + 1
        q.append(day)

    days = 0  # 진행일 수
    while q:
        count = 0
        for day in list(q):  # deque 크기 유지를 위해 list로 복사
            if day > days:
                break
            q.popleft()
            count += 1
        if count:
            answer.append(count)
        days += 1
    return answer
