def solution(bandage, health, attacks):
    status = health # 현재 체력
    cnt = 0 # 연속 성공 횟수
    time = 0 # 현재 시간
    while attacks:
        t, damage = attacks.pop(0) # 공격 시간, 데미지
        # 공격 전까지 회복
        for i in range(time + 1, t):
            time += 1
            status = min(health, status + bandage[1])
            cnt += 1
            if cnt == bandage[0]: # 시전 시간동안 충전
                status = min(health, status + bandage[2])
                cnt = 0
        # 공격 당함
        status -= damage
        if status <= 0: # 사망
            return -1
        cnt = 0
        time += 1
    return status