import sys
input = sys.stdin.readline


def solution(command, x, y, location, nums):
    dx, dy = list(directs[command])
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < m:  # 가능
        if command == 1:  # 동
            num = 3
            index1 = location.index(num)  # 동
            index2 = location.index(1)  # 상
        elif command == 2:  # 서
            num = 4
            index1 = location.index(num)  # 서
            index2 = location.index(1)  # 상
        elif command == 3:  # 북
            num = 5
            index1 = location.index(num)  # 뒤
            index2 = location.index(1)  # 상
        else:  # 남
            num = 2
            index1 = location.index(num)  # 앞
            index2 = location.index(1)  # 상

        # 위치 변경
        location[index1], location[7 - index1] = 6, 1
        location[index2], location[7 - index2] = num, 7 - num

        # 칸의 숫자 변경
        if array[nx][ny] == 0:  # 칸의 숫자 0
            array[nx][ny] = nums[index1]
        else:  # 칸의 숫자 0 아님
            nums[index1] = array[nx][ny]
            array[nx][ny] = 0

        print(nums[7 - index1])
        return nx, ny
    else:  # 불가능
        return x, y


n, m, x, y, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
directs = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동, 서, 북, 남
nums = [0] * 7  # 해당 위치 별 숫자
location = [0, 1, 2, 3, 4, 5, 6]  # 각 위치 : 상, 앞, 우, 좌, 뒤, 하

for command in commands:
    x, y = solution(command, x, y, location, nums)
