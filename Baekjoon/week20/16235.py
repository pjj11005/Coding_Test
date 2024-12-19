import sys
input = sys.stdin.readline

# 봄과 여름 겨울 처리 함수
def spring_summer_winter():
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                new_trees = {}  # 살아 남은 나무들
                dead_trees = 0  # 죽은 나무 양분 값들
                no_tree = False  # 추가할 나무 없음음
                for age, count in sorted(tree[i][j].items()):
                    can_survive = land[i][j] // age  # 해당 나무로 살아남을 수 있는 나무의 수
                    if no_tree:  # 모두 양분으로로
                        dead_trees += count * (age // 2)
                    elif can_survive >= count:  # 모든 나무 생존
                        land[i][j] -= age * count
                        new_trees[age + 1] = count
                    else:  # 일부 나무만 생존
                        no_tree = True
                        land[i][j] -= age * can_survive
                        new_trees[age + 1] = can_survive
                        dead_trees += (count - can_survive) * (age // 2)

                tree[i][j] = new_trees  # 살아남은 나무 갱신
                land[i][j] += dead_trees

            # 겨울: 양분 추가
            land[i][j] += feed[i][j]

# 가을 처리 함수
def fall():
    for i in range(n):
        for j in range(n):
            new_tree = 0
            # 가을: 나이가 5의 배수인 나무 번식
            for age, count in tree[i][j].items():
                if age % 5 == 0:
                    new_tree += count
            if new_tree:  # 번식 가능
                for dx, dy in move:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if 1 in tree[nx][ny]:  # 이미 번식한 나무 존재
                            tree[nx][ny][1] += new_tree
                        else:  # 처음 번식하는 나무
                            tree[nx][ny][1] = new_tree


# 입력 처리
n, m, k = map(int, input().split())
feed = [list(map(int, input().split())) for _ in range(n)]  # 겨울에 추가되는 양분
land = [[5] * n for _ in range(n)]  # 초기 양분은 5로 설정
tree = [[{} for _ in range(n)] for _ in range(n)]  # 각 칸에 있는 나무 정보
move = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

# 초기 나무 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1][z] = 1

# K년 동안 시뮬레이션 실행
for _ in range(k):
    spring_summer_winter()
    fall()

# 살아있는 나무 개수 계산
result = sum(sum(tree[i][j].values()) for i in range(n) for j in range(n))
print(result)