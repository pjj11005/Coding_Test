import sys
from math import dist

input = sys.stdin.readline


# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 서로 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution():
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    parent = list(range(n + 1))  # 부모 노드 저장
    answer = 0

    # 모든 간선 저장
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            edges.append((d, i + 1, j + 1))

    # 간선 길이 순 정렬
    edges.sort()

    # 최소 거리 순 연결
    for d, a, b in edges:
        # 사이클 없으면
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += d

    print(round(answer, 2))


if __name__ == "__main__":
    solution()
