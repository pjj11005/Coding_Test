import sys
input = sys.stdin.readline

answer = 0
visited_y = []
for i in range(int(input())):
    x, y = map(int, input().split())
    if not visited_y:
        visited_y.append(y)
    else:
        while visited_y:
            stack_y = visited_y.pop()
            if stack_y < y: # 큰 높이가 오면 스택에 추가
                visited_y.append(stack_y)
                visited_y.append(y)
                break
            elif stack_y > y: # 낮은 높이 오면 answer 증가
                if not visited_y: # 만약 비어있으면 새롭게 추가
                    visited_y.append(y)
                answer += 1
            else: # 높이 같으면 추가 안함
                visited_y.append(stack_y)
                break
        
while visited_y: # 만약 스택에 0보다 큰 높이가 있으면 answer 증가
    stack_y = visited_y.pop()
    if stack_y > 0:
        answer += 1
print(answer)