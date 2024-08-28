SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
    FROM DEVELOPERS
    WHERE
        skill_code & (
            SELECT SUM(code)
            FROM SKILLCODES
            WHERE NAME IN ("Python", "C#")
        ) != 0
    ORDER BY ID;