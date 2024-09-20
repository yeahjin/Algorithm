-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME from animal_outs as a
left join animal_ins as b using(ANIMAL_ID)
where b.datetime is null
order by a.ANIMAL_ID, a.NAME