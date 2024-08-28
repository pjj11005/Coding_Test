import sys
input = sys.stdin.readline

def solution():
    count = [0] * 21
    for i in range(int(input())):
        array = list(input().strip().split())
        if array[0] == 'all':
            count = [1] * 21
        elif array[0] == 'empty':
            count = [0] * 21
        else:
            array[1] = int(array[1])
            if array[0] == 'check':
                if count[array[1]]:
                    print(1)
                else:
                    print(0)
            elif array[0] == 'add':
                if count[array[1]] == 0:
                    count[array[1]] = 1
            elif array[0] == 'remove':
                if count[array[1]] == 1:
                    count[array[1]] = 0
            elif array[0] == 'toggle':
                if count[array[1]] == 1:
                    count[array[1]] = 0
                else:
                    count[array[1]] = 1
solution()