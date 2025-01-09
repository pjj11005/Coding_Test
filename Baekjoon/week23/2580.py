import sys

input = sys.stdin.readline

# 행 체크
def check_row(x, num, array):
	for i in range(9):
		if array[x][i] == num:
			return False
	return True

# 열 체크
def check_col(y, num, array):
	for i in range(9):
		if array[i][y] == num:
			return False
	return True

# 정사각형 체크
def check_square(x, y, num, array):
	a, b = (x // 3) * 3, (y // 3) * 3
	for i in range(3):
		for j in range(3):
			if array[a + i][b + j] == num:
				return False
	return True
	
def dfs(idx, array, blanks):
	if idx == len(blanks):
		for row in array:
			print(*row)
		exit(0)
	
	x, y = blanks[idx]
	for num in range(1, 10):
		if check_row(x, num, array) and check_col(y, num, array) and check_square(x, y, num, array):
			array[x][y] = num
			dfs(idx + 1, array, blanks)
			array[x][y] = 0

def main():
    array = [list(map(int, input().split())) for _ in range(9)]
    blanks = [(i, j) for i in range(9) for j in range(9) if array[i][j] == 0]
    
    dfs(0, array, blanks)

if __name__ == '__main__':
    main()
