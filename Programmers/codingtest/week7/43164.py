def dfs(start, depth, tickets, n, temp, visited, answer):
    if depth == n:
        if not answer or temp < answer:  # 사전순으로 더 빠른 경우에만 업데이트
            answer.clear()  # 기존 값을 비우고
            answer.extend(temp)  # 새 경로를 할당
        return
    
    for i, ticket in enumerate(tickets):
        x, y = ticket
        if (start == x) and not visited[i]:
            visited[i] = 1
            temp.append(y)
            dfs(y, depth + 1, tickets, n, temp, visited, answer)
            visited[i] = 0
            temp.pop()
            
def solution(tickets):
    answer = []
    n = len(tickets)
    tickets.sort()
        
    visited = [0] * n
    dfs('ICN', 0, tickets, n, ['ICN'], visited, answer)

    return answer