-- 코드를 입력하세요
SELECT distinct CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY as h
join CAR_RENTAL_COMPANY_CAR as c using(CAR_ID)
where c.car_type = "세단" and MONTH(start_date) = 10
order by car_id desc