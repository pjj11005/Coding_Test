'''permutations: 44ms'''
import sys
from itertools import permutations

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    print('\n'.join(map(' '.join, permutations(map(str, range(1, n+1)), m))))   


if __name__ == '__main__':
    solution()


'''DFS: 168ms
import sys

input = sys.stdin.readline


def dfs(temp, n, m, visited):
	# 길이가 m이면 출력
	if len(temp) == m:
		print(*temp)
		return
	
	# 가능한 수열 찾기
	for i in range(1, n + 1):
		if not visited[i]:
			visited[i] = 1
			temp.append(i)
			dfs(temp, n, m, visited)
			visited[i] = 0
			temp.pop()


def solution():
    n, m = map(int, input().split())
    visited = [0] * (n + 1)
    dfs([], n, m, visited)


if __name__ == '__main__':
    solution()
'''
