SELECT COUNT(*) AS USERS
    FROM USER_INFO
    WHERE (AGE >= 20 AND AGE < 30) AND (JOINED LIKE '2021%') # 나이 20대 AND 가입 날짜 2021년도
