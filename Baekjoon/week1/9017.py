import sys
input = sys.stdin.readline

def solution(n, array):
    dict = {}
    answer = []
    num = [0] * 201
    team = []
    count = 1
    for a in array:
        num[a] += 1
    
    for i in range(1, 201):
        if num[i] == 6:
            team.append(i)
    
    for a in array: # 참가 팀 점수 저장
        if a in team:
            dict[a] = dict.get(a, [])
            dict[a].append(count)
            count += 1
    
    for num, num_list in dict.items(): # 팀별 점수 기준 정렬
        answer.append((sum(num_list[:4]), num_list[4], num))
    
    answer = sorted(answer, key=lambda x:(x[0], x[1]))
    
    return answer[0][2]

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    print(solution(n, array))