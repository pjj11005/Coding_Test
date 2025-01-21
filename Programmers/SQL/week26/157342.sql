SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY CAR_ID
    HAVING AVERAGE_DURATION >= 7
    ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC
# DATEDIFF : 날짜 차이(일수 차이), GROUP BY 묶은 후 조건은 HAVING으로
