-- 코드를 입력하세요
SELECT i.animal_id, i.name from animal_ins as i
join animal_outs as o using(animal_id)
order by abs(datediff(i.datetime, o.datetime)) + 1 desc limit 2