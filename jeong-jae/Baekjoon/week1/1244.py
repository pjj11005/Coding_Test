import sys

input = sys.stdin.readline

def change(s, num, array):
    if s == 1: # 남자
        idx = num - 1
        while True:
            if idx >= len(array):
                break
            array[idx] = 1 - array[idx]
            idx += num
    else: # 여자
        idx = num - 1
        array[idx] = 1 - array[idx]
        left, right = idx - 1, idx + 1
        while True:
            if left < 0 or right >= len(array):
                break

            if array[left] == array[right]:
                array[left] = 1 - array[left]
                array[right] = 1 - array[right]
            else:
                break
            left -= 1
            right += 1
    
    return array

def solution():
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        s, num = map(int, input().split())
        array = change(s, num, array)
    
    count, rest = len(array) // 20,  len(array) % 20
    if rest == 0:
        for i in range(count):
            temp = array[20 * i : 20 * (i + 1)]
            for t in temp:
                print(t, end=' ')
            print()
    else:
        for i in range(count + 1):
            if i == count: # 마지막
                temp = array[20 * count:]
                for t in temp:
                    print(t, end=' ')
                print()
            else:
                temp = array[20 * i: 20 * (i + 1)]
                for t in temp:
                    print(t, end=' ')
                print()

solution()