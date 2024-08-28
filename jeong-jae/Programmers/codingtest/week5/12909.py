from collections import deque

def solution(s):
    q = deque()
    stack = list(s)
    while stack:
        string = stack.pop()
        q.appendleft(string)
        if len(q) >= 2 and q[0] == '(' and q[1] == ')':  # 괄호
            q.popleft()
            q.popleft()
    if q:  # False
        return False
    else:  # True
        return True