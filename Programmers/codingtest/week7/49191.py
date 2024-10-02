def solution(n, results):
    answer = 0
    # 간선 정보 저장
    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = 1
        graph[b][a] = -1
    # 자기 자신 = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
    # 플로이드 워셜            
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][k] == 1 and graph[k][b] == 1: # 승리 + 승리
                    graph[a][b] = 1
                elif graph[a][k] == -1 and graph[k][b] == -1: # 패배 + 패배
                    graph[a][b] = -1
    # 순위 매길 수 있는 선수 카운트
    for i in range(1, n + 1):
        if graph[i][1:].count(int(1e9)) == 0:
            answer += 1
                  
    return answer