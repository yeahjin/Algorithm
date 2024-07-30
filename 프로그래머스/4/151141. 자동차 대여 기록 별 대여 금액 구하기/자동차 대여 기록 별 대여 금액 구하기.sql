WITH ta AS (
    SELECT 
        history_id, 
        ABS(DATEDIFF(start_date, end_date)) + 1 AS d, 
        c.daily_fee
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY AS h
    JOIN 
        CAR_RENTAL_COMPANY_CAR AS c USING(car_id)
    WHERE 
        c.car_type = "트럭"
),
b AS (
    SELECT 
        d, 
        history_id,
        CASE
            WHEN d >= 90 THEN "90일 이상"
            WHEN d >= 30 THEN "30일 이상"
            WHEN d >= 7 THEN "7일 이상"
            ELSE "7일 미만"
        END AS date_name
    FROM 
        ta
)

SELECT 
    ta.history_id, 
    CASE
        WHEN discount_rate IS NOT NULL THEN ROUND(ta.daily_fee * ta.d * (100 - discount_rate) / 100, 0)
        ELSE ta.daily_fee * ta.d
    END AS FEE
FROM 
    ta
LEFT JOIN 
    b ON ta.history_id = b.history_id
LEFT JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
ON 
    b.date_name = CAR_RENTAL_COMPANY_DISCOUNT_PLAN.DURATION_TYPE
WHERE 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN.CAR_TYPE = "트럭" OR
    b.date_name = "7일 미만"
ORDER BY 
    FEE DESC, 
    b.history_id DESC;

