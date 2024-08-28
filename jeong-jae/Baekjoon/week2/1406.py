import sys
from collections import deque

input = sys.stdin.readline

def solution(m, text):
    left = deque(text) # 커서를 기준으로 deque를 각자 따로 둔다
    right = deque()

    for _ in range(m):
        command = input().strip()
        if command[0] == 'L' and left:
            right.appendleft(left.pop())
        elif command[0] == 'D' and right:
            left.append(right.popleft())
        elif command[0] == 'B' and left:
            left.pop()
        elif command[0] == 'P':
            left.append(command[2])

    return ''.join(left) + ''.join(right)

text = input().strip()
m = int(input())
print(solution(m, text))