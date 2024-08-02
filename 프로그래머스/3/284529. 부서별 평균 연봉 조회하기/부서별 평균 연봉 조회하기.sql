-- 코드를 작성해주세요
with a as (select dept_id,round(avg(sal)) as AVG_SAL from hr_employees
group by dept_id)

select dept_id, dept_name_en, avg_sal from a
join hr_department using(dept_id)
order by avg_sal desc