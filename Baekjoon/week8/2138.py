import sys
input = sys.stdin.readline

def solution(n, s1, goal):
    answer1 = 0
    answer2 = 0
    if s1 == goal:
        return 0
    
    s2 = s1.copy() # 복사
    
    # 첫번째 누르기
    s1[0] = 1 - s1[0]
    s1[1] = 1 - s1[1]
    answer1 += 1
    for i in range(1, n):
        if i == n - 1:
            if s1[i - 1] != goal[i - 1]:
                s1[i - 1] = 1 - s1[i - 1]
                s1[i] = 1 - s1[i]
                answer1 += 1
        else:
            if s1[i - 1] != goal[i - 1]:
                s1[i - 1] = 1 - s1[i - 1]
                s1[i] = 1 - s1[i]
                s1[i + 1] = 1 - s1[i + 1]
                answer1 += 1
    
    if s1 != goal: # 완성 X
        answer1 = -1
    
    # 첫번째 누르지 않기
    for i in range(1, n):
        if i == n - 1:
            if s2[i - 1] != goal[i - 1]:
                s2[i - 1] = 1 - s2[i - 1]
                s2[i] = 1 - s2[i]
                answer2 += 1
        else:
            if s2[i - 1] != goal[i - 1]:
                s2[i - 1] = 1 - s2[i - 1]
                s2[i] = 1 - s2[i]
                s2[i + 1] = 1 - s2[i + 1]
                answer2 += 1
    
    if s2 != goal: # 완성 X
        answer2 = -1
    
    if answer1 == -1 and answer2 == -1: # 불가능
        return -1
    elif answer1 > 0 and answer2 == -1:
        return answer1
    elif answer1 == -1 and answer2 > 0:
        return answer2
    else:
        return min(answer1, answer2)
        
n = int(input())
s1 = list(map(int, input().strip()))
goal = list(map(int, input().strip()))
print(solution(n, s1, goal))