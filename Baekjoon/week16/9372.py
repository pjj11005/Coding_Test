import sys
input = sys.stdin.readline

# 테스트 케이스의 수 입력
T = int(input())

for _ in range(T):
    # 국가의 수 N과 비행기의 종류 M 입력
    N, M = map(int, input().split())
    
    # 비행기 경로는 읽기만 하고 사용하지 않음
    for _ in range(M):
        a, b = map(int, input().split())
    
    # 최소 비행기 수는 항상 N - 1
    print(N - 1)


''' 신장 트리 풀이(내 풀이)
import sys
input = sys.stdin.readline
# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
# 부모 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    edges = [] # 간선 저장 리스트
    answer = 0
    for i in range(m): # 간선 저장
        a, b = map(int, input().split())
        edges.append((a, b))
        
    edges.sort()
    for a, b in edges:
        # 사이클 발생 안할 때 answer + 1
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += 1
    print(answer)
'''