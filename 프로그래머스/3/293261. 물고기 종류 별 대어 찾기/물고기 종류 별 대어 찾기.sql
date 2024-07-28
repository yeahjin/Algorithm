-- 코드를 작성해주세요
with max_length as (
select n.fish_type, n.fish_name ,max(length) as LENGTH
from fish_info as i
inner join fish_name_info as n on i.fish_type = n.fish_type
group by i.fish_type, n.fish_name
)

select i.id, m.fish_name, m.length from max_length as m
join fish_info as i on i.length = m.length
and i.fish_type = m.fish_type
order by i.id