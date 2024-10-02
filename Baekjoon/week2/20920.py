import sys
input = sys.stdin.readline

def solution(n, m):
    count = {}
    answer = []
    for i in range(n):
        word = input().strip()
        if len(word) >= m: # 길이 m 이상의 단어
            if word not in count.keys(): # 처음 
                count[word] = 1
            else: # 존재
                count[word] += 1
    
    for word in count.keys():
        answer.append((count[word], len(word), word))

    sorted_answer = sorted(answer, key=lambda x : (-x[0], -x[1], x[2])) # 빈도수/길이/사전

    for c, l, w in sorted_answer:
        print(w)

n, m = map(int, input().split())
solution(n, m)