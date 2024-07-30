-- 코드를 입력하세요
SELECT HISTORY_ID, CAR_ID, date_format(start_date,"%Y-%m-%d") as START_DATE, date_format(end_date, "%Y-%m-%d") as END_DATE,
case
    when abs(datediff(start_date, end_date))+1 >= 30 then "장기 대여"
    else "단기 대여"
end as RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where YEAR(start_date) = 2022 and MONTH(start_date) = 9
order by history_id desc