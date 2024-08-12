import sys
input = sys.stdin.readline

def solution(count):
    global answer
    keywords = list(input().strip().split(','))
    for keyword in keywords:
        if (keyword in count.keys()) and count[keyword] == 0: # 메모장에 있고 지워지지 않은 키워드이면
            count[keyword] += 1
            answer -= 1

n, m = map(int, input().split())
count = {}
answer = n
for i in range(n):
    key = input().strip()
    count[key] = 0

for i in range(m):
    if answer > 0:
        solution(count)
    print(answer)