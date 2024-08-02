-- 코드를 작성해주세요
with a as(select fish_type, count(*) as FISH_COUNT from fish_info
group by fish_type)

select fish_count, fish_name from a
left join fish_name_info using(fish_type)
order by fish_count desc