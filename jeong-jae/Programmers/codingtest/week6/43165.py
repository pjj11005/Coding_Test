def dfs(numbers, target, total, depth, answer):
    if depth == len(numbers):
        if total == target:
            answer[0] += 1
        return
    
    dfs(numbers, target, total + numbers[depth], depth + 1, answer)
    dfs(numbers, target, total - numbers[depth], depth + 1, answer)

def solution(numbers, target):
    answer = [0]
    dfs(numbers, target, numbers[0], 1, answer)
    dfs(numbers, target, -numbers[0], 1, answer)
    
    return answer[0]
