-- 코드를 입력하세요
SELECT ANIMAL_ID, name, date_format(DATETIME, "%Y-%m-%d") as "날짜" from animal_ins
order by animal_id