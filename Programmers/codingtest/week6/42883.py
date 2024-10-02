def solution(number, k):
    answer = ''
    number = list(number)
    n = len(number)
    m = len(number) - k
    count = 0
    stack = []
    for n in number:
        while stack and count < k and stack[-1] < n:
            stack.pop()
            count += 1
        stack.append(n)
    if len(stack) > m:
        stack.pop()
    answer = ''.join(stack)
    return answer