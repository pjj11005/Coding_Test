import sys
input = sys.stdin.readline

def solution():
    n, k, t, m = map(int, input().split())
    score = [[0] * (k + 1) for _ in range(n + 1)] # 점수
    count = [0] * (n + 1) # 제출 횟수
    time = [0] * (n + 1) # 제출 시간
    answer = []
    for a in range(m):
        i, j, s = map(int, input().split())
        if score[i][j] < s: # 점수 변경
            score[i][j] = s
        count[i] += 1
        time[i] = a
    
    for num in range(1, n + 1):
        answer.append((sum(score[num]), count[num], time[num], num))

    sorted_answer = sorted(answer, key=lambda x: (-x[0], x[1], x[2])) # 점수/횟수/시간

    for rank in range(n):
        if sorted_answer[rank][3] == t:  # 팀 등수
            return rank + 1
            
T = int(input())
for x in range(T):
    print(solution())