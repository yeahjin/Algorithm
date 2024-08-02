-- 코드를 작성해주세요
with a as(select 
case
    when length is null then 10
    else length
end as LENGTH,
ID, FISH_TYPE, TIME from fish_info),

b as (select fish_type ,avg(length) as a, count(*) as fish_count, max(length) as m from a 
      group by fish_type
          )
# c as (
# select fish_type, avg(length)
# )
          
select fish_count, m as MAX_LENGTH, FISH_TYPE from b
where a >= 33
order by fish_type