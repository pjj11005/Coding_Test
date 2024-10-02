import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)  # 재귀 제한을 너무 크게 하지 않음

def dfs(x, y):
    if x == y:  # 도착할 목표 노드에 도달한 경우
        return True

    visited[x] = True  # 현재 노드를 방문 처리

    for i in range(n):
        if array[x][i] == 1 and not visited[i]:  # 연결되어 있고 아직 방문하지 않은 노드 탐색
            if dfs(i, y):  # 목표 노드까지 도달하면 True 반환
                return True

    return False  # 목표 노드에 도달하지 못한 경우

n = int(input())  # 도시의 수
m = int(input())  # 여행 계획에 포함된 도시의 수
array = [list(map(int, input().split())) for _ in range(n)]  # 연결 정보 (인접 행렬)
goal = list(map(int, input().split()))  # 여행 계획에 포함된 도시들

answer = 'YES'
for i in range(m - 1):
    visited = [False] * n  # 방문 여부 초기화
    if not dfs(goal[i] - 1, goal[i + 1] - 1):  # 각 연속된 도시들이 연결되어 있는지 확인
        answer = 'NO'
        break

print(answer)
