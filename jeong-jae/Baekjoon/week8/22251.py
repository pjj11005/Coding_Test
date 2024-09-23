import sys
input = sys.stdin.readline

def solution(N, K, P, X, array):
    answer = -1 # 자기 자신 제외
    # 변환 횟수 저장 테이블
    change = [[0] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(i + 1, 10):
            count = 0
            for k in range(7):
                if array[i][k] != array[j][k]:
                    count += 1
            change[i][j] = count
            change[j][i] = count
    
    # 변환 수행
    X = list(map(int, str(X).zfill(K))) # 나머지 부분 0으로 채우고 리스트로 변환
    for value in range(1, N + 1):
        value = list(map(int, str(value).zfill(K)))
        count = 0
        for i in range(K):
            count += change[X[i]][value[i]]
        
        if count <= P: # P번 이하의 변환 횟수
            answer += 1
    
    return answer

N, K, P, X = map(int, input().split())
# 숫자 배열
array = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0],
         [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
print(solution(N, K, P, X, array))