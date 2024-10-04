import sys
input = sys.stdin.readline

def solution(n, array):
    answer = 0
    if n == 1: # 건물 1개일 때
        return answer
    
    for i in range(n):
        count = 0
        for j in range(i): # 앞쪽 건물
            a = (array[i] - array[j]) / (i - j) # 특정 건물과의 기울기
            flag = True
            for k in range(j + 1, i):
                b = (array[i] - array[k]) / (i - k) # 비교할 건물의 기울기
                if a >= b: # 안보임
                    flag = False
                    break
            if flag: # 보임
                count += 1
                    
        for j in range(i + 1, n): # 뒤쪽 건물
            a = (array[j] - array[i]) / (j - i) # 특정 건물과의 기울기
            flag = True
            for k in range(i + 1, j):
                b = (array[k] - array[i]) / (k - i) # 비교할 건물의 기울기
                if a <= b: # 안보임
                    flag = False
                    break
            if flag: # 보임
                count += 1
                
        answer = max(answer, count)
    return answer

n = int(input())
array = list(map(int, input().split()))
print(solution(n, array))