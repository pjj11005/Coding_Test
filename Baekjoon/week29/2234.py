import sys
from collections import deque

input = sys.stdin.readline


# BFS : 1, 2번 답 구하는 함수
def bfs(i, j, n, m, array, visited, answer, move):
    q = deque([(i, j)])
    visited[i][j] = answer[0]
    size = 0  # 방의 크기

    while q:
        x, y = q.popleft()
        size += 1

        for z in range(4):
            if array[x][y][z] == "0":  # 점선
                nx, ny = x + move[z][0], y + move[z][1]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = answer[0]
                    q.append((nx, ny))

    return size


# 3번 구하는 함수
def solution_3(n, m, visited, roomsize):
    max_size = 0  # 답
    check = [(1, 0), (0, 1)]  # 남, 동 쪽으로 인접한 경우만 체크

    for i in range(m):
        for j in range(n):
            for di, dj in check:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and visited[i][j] != visited[ni][nj]:
                  max_size = max(max_size, roomsize[visited[i][j]] + roomsize[visited[ni][nj]])

    return max_size

def solution():
  n, m = map(int, input().split())
  array = [list(map(lambda x: list(bin(int(x))[2:].zfill(4)), input().split())) for _ in range(m)]  # 이진수로 변환하여 입력 받음
  visited = [[0] * n for _ in range(m)]  # 방 번호 배열 - 각 위치에 방의 번호 저장
  move = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 이동
  roomsize = [0]  # 각 방의 크기 저장 배열 - 1번 부터
  answer = [0, 0, 0]  # 1, 2, 3번 답

  # 1번, 2번
  for i in range(m):
      for j in range(n):
          if not visited[i][j]:
              answer[0] += 1  # 방의 번호, 개수 파악
              size = bfs(i, j, n, m, array, visited, answer, move)
              roomsize.append(size)
              answer[1] = max(answer[1], size)  # 최대 크기 방 구하기


  # 3번
  answer[2] = solution_3(n, m, visited, roomsize)

  for a in answer:
      print(a)
    
  
if __name__ == '__main__':
  solution()
