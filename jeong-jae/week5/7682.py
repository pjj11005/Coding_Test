import sys

input = sys.stdin.readline

def check(array, x_count, o_count):  # 가로, 세로, 대각선 체크
    x_check, o_check = False, False
    for i in range(3): # 가로
        if array[i].count('X') == 3 or array[i].count('O') == 3:
            if array[i][0] == 'X':
                x_check = True
            else:
                o_check = True
    
    for i in range(3): # 세로
        temp = []
        for j in range(3):
            temp.append(array[j][i])
        if temp.count('X') == 3 or temp.count('O') == 3:
            if temp[0] == 'X':
                x_check = True
            else:
                o_check = True
    
    for i in range(2):  # 대각선
        if i == 0:
            if array[1][1] == array[0][0] and array[1][1] == array[2][2]:
                if array[1][1] == 'X':
                    x_check = True
                else:
                    o_check = True
        else:
            if array[1][1] == array[0][2] and array[1][1] == array[2][0]:
                if array[1][1] == 'X':
                    x_check = True
                else:
                    o_check = True
    
    if x_check == True and o_check == True:  # T / T
        return False
    elif x_check == True and o_check == False:  # T / F
        if x_count > o_count:  
            return True
        else:
            return False
    elif x_check == False and o_check == True:  # F / T
        if x_count == o_count:  
            return True
        else:
            return False
    else: # F / F
        if x_count + o_count == 9: # 가득 참
            return True
        return False
    
def solution(s):
    array = []
    x_count, o_count = 0, 0
    for i in range(3): # 게임판 만들기
        temp = []
        for j in range(3):
            if s[(3 * i) + j] == 'X':
                x_count += 1
            elif s[(3 * i) + j] == 'O':
                o_count += 1
            temp.append(s[(3 * i) + j])
        array.append(temp)
    
    if x_count == o_count or x_count == o_count + 1: # 갯수 맞음
        if check(array, x_count, o_count):
            return 'valid'
        else:
            return 'invalid'
    else: # 갯수 안맞음
        return 'invalid'
    
while True:
    s = input().strip()
    if s == 'end': # 종료
        break
    else:
        print(solution(s))

'''
- X와 O가 조건을 만족할 때를 모두 확인해야함
- 명확하게 조건을 나누어줘야 함
'''