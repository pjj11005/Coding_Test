import sys

input = sys.stdin.readline

def solution():
    h, w, x, y = map(int, input().split())
    array = [list(map(int, input().split()))[:w] for _ in range(h)] # A 배열의 크기만큼만 입력 받음
    
    # 겹친 부분만 제거해준다
    for i in range(h - x):
        for j in range(w - y):
            array[i + x][j + y] -= array[i][j]
    
    for row in array:
        print(*row)
        
        
if __name__ == '__main__':
    solution()
