import sys
input = sys.stdin.readline

def solution(n, k, array):
    answer = []
    start, end = 0, 0
    for i in range(n):
        if array[i] == 'P': # 사람 일 때
            if i - k < 0: # 왼쪽
                start = 0
            else:
                start = i - k
            
            if i + k > n - 1: # 오른쪽
                end = n - 1
            else:
                end = i + k
            
            if answer: # 저장한 햄버거 위치 존재 O
                if start <= answer[-1] <= end: # 시작 지점 변경
                    start = answer[-1] + 1
                elif end < answer[-1]: # 탐색할 필요 없음
                    continue

            for j in range(start, end + 1):
                if i == j or array[j] == 'P': # 본인 위치 or 사람
                    continue
                elif array[j] == 'H' and (j not in answer): # 추가된적 없는 햄버거 위치 추가 
                    answer.append(j)
                    break
    return len(answer)

n, k = map(int, input().split())
array = list(input().strip())
print(solution(n, k, array))