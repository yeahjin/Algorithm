-- 코드를 작성해주세요
with a as(
select emp_no, sum(score) as score from hr_grade
group by emp_no
order by score desc limit 1)

select a.SCORE, a.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL from a
inner join HR_EMPLOYEES as e on a.emp_no = e.emp_no