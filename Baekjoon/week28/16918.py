import sys

input = sys.stdin.readline


def bomb(r, c, n, array, direct):
    new_array = [['O'] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if array[x][y] == 'O':
                new_array[x][y] = '.'
                for dx, dy in direct:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        new_array[nx][ny] = '.'
        
    return new_array


def solution():
    r, c, n = map(int, input().split())
    array = [list(input().strip()) for _ in range(r)]
    direct = ((0, 1), (0, -1), (-1, 0), (1, 0))
    
    if n == 1:
        for row in array:
            print(''.join(row))
    elif n % 2 == 0:
        for i in range(r):
            print('O' * c)
    else:
        array = bomb(r, c, n, array, direct)          
        # 한번만 폭발
        if n % 4 == 3:
            for row in array:
                print(''.join(row))
        # 한번 더 폭발
        else:
            array = bomb(r, c, n, array, direct)
            for row in array:
                print(''.join(row))


if __name__ == '__main__':
    solution()
