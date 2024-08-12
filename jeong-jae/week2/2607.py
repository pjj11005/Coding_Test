import sys
input = sys.stdin.readline

def solution(str1, str2):
    count = abs(len(str1) - len(str2))
    if count >= 2: # 길이 차이 2 이상
        return 0
    elif len(str1) >= len(str2):
        count = 0

    check = [0] * len(str2)
    for i in range(len(str1)):
        flag = False
        for j in range(len(str2)):
            if str1[i] == str2[j] and check[j] == 0: # 같은 문자 and 차감 X
                check[j] += 1
                flag = True
                break
        if not flag: # 차이점 +1
            count += 1
        
        if count >= 2: # 차이점 2 이상
            return 0
    return 1

n = int(input())
array = [input().strip() for _ in range(n)]
answer = 0
for i in range(1, n):
    answer += solution(array[0], array[i])
print(answer)