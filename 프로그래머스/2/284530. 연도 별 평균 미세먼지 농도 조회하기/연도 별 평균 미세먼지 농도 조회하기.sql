-- 코드를 작성해주세요
SELECT 
    YEAR(YM) AS YEAR,
    round(avg(pm_val1), 2) AS PM10, 
    ROUND(AVG(pm_val2), 2) AS "PM2.5"
FROM 
    air_pollution
WHERE  LOCATION2 = '수원'
GROUP BY 
    YEAR(YM)
ORDER BY 
    YEAR(YM);