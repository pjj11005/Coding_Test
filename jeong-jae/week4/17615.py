import sys
input = sys.stdin.readline

def jump(color, direct, s):
    count = 0
    color_count = 0
    if direct == 'front':
        for i in range(n):
            if s[i] == color:
                color_count += 1
            if s[i] != color and color_count:
                count += color_count
                color_count = 0
                
    else: # 뒤로
        for i in range(n):
            if s[i] == color:
                color_count += 1
            if s[i] != color and color_count:
                count += color_count
                color_count = 0

    return count

def solution(n, s):
    if len(set(s)) == 1: # 한 문자로만 이루어짐
        return 0
    answer = int(1e9)
    for i in range(4):
        if i == 0: # R 뒤로
            answer = min(answer, jump('R', 'back', s))
        elif i == 1:  # B 뒤로
            answer = min(answer, jump('B', 'back', s))
        elif i == 2:  # R 앞으로
            s.reverse()
            answer = min(answer, jump('R', 'front', s))
        else: # B 앞으로
            answer = min(answer, jump('B', 'front', s))
    return answer

n = int(input())
s = list(input().strip())
print(solution(n, s))