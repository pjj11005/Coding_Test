def find_parent(parent, x):  # 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):  # 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, wires):
    answer = int(1e9)
    n = len(wires) + 1

    for idx in range(len(wires)):  # 제거할 전선
        parent = [i for i in range(n + 1)]  # 부모 노드
        for i, wire in enumerate(wires):
            if i != idx:  # 연결된 전선일때
                a, b = wire
                union_parent(parent, a, b)

        parent = [find_parent(parent, i) for i in range(1, n + 1)]
        count = abs(parent.count(max(parent)) - parent.count(min(parent)))
        answer = min(answer, count)
    return answer
