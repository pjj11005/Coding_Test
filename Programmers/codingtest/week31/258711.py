from collections import defaultdict


def solution(edges):
    edge_counts = defaultdict(lambda: [0, 0])  # 나가는 간선의 수, 들어오는 간선의 수
    for a, b in edges:
        edge_counts[a][0] += 1
        edge_counts[b][1] += 1

    # 각 그래프 유형 카운트
    created_node = donut = stick = eight = 0
    for key, value in edge_counts.items():
        # 생성 정점
        if value[0] >= 2 and value[1] == 0:
            created_node = key
        # 막대 모양 그래프의 수
        elif value[0] == 0 and value[1] > 0:
            stick += 1
        # 8자 모양 그래프의 수
        elif value[0] == 2 and value[1] >= 2:
            eight += 1
    # 도넛 모양 그래프의 수
    donut = edge_counts[created_node][0] - (stick + eight)

    return [created_node, donut, stick, eight]
