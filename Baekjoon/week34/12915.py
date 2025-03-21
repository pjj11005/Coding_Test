import sys

input = sys.stdin.readline


# 이분 탐색
def solution2():
    e, em, m, mh, h = map(int, input().split())

    start, end = 0, min(e + em, em + m + mh, mh + h)

    while start <= end:
        mid = (start + end) // 2

        # 각 문제 필요량
        easy_needed = mid_needed = hard_needed = mid

        # easy
        if e >= easy_needed:  # e로 다 가능 -> em 필요 없음
            easy_em_used = 0
        else:
            easy_em_used = easy_needed - e
            if easy_em_used > em:  # em 필요량이 em 보다 많음
                end = mid - 1
                continue

        # hard
        if h >= hard_needed:  # h로 다 가능 -> mh 필요 없음
            hard_mh_used = 0
        else:
            hard_mh_used = hard_needed - h
            if hard_mh_used > mh:
                end = mid - 1
                continue

        # mid
        em_left = em - easy_em_used
        mh_left = mh - hard_mh_used

        # mid 커버 가능
        if em_left + m + mh_left >= mid_needed:
            start = mid + 1
        # mid 부족
        else:
            end = mid - 1

    print(end)


# 그리디
def solution():
    e, em, m, mh, h = map(int, input().split())
    answer = 0

    while True:
        # easy
        if e > 0:
            e -= 1
        elif em > 0:
            em -= 1
        else:
            break

        # medium
        if m > 0:
            m -= 1
        else:  # em과 mh 중에서 더 많은 것 선택
            if em > 0 and em >= mh:
                em -= 1
            elif mh > 0:
                mh -= 1
            else:
                break

        # hard
        if h > 0:
            h -= 1
        elif mh > 0:
            mh -= 1
        else:
            break

        answer += 1

    print(answer)


if __name__ == "__main__":
    solution2()
