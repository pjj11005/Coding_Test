import sys
input = sys.stdin.readline

def solution(p, m, array):
    answer = []
    for l, n in array:
        flag = False
        if not answer: # 매칭 가능한 방 없음
            temp = []
            temp.append((l, n))
            answer.append(temp)
        else: # 매칭 가능한 방 있음
            for a in answer:
                if flag: # 방에 참가
                    break

                if len(a) < m and (a[0][0] - 10 <= l <= a[0][0] + 10) and not flag: # 입장 가능
                    a.append((l, n))
                    flag = True
            
            # 방을 다 돌았는데 들어간 곳이 없다면 생성
            if not flag:
                temp = []
                temp.append((l, n))
                answer.append(temp)

    for a in answer:
        sorted_a = sorted(a, key=lambda x:x[1])

        if len(sorted_a) == m: # 시작
            print('Started!')
        else: # 대기
            print('Waiting!') 

        for l, n in sorted_a: # 정보 출력
            print(l, n)

p, m = map(int, input().split())
array = []
for i in range(p):
    l, n = input().strip().split()
    array.append((int(l), n))
solution(p, m, array)