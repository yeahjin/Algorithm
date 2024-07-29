with  length_value as (select
    case
        when length is null then 10
        else length
    end as length
from fish_info)

select round(sum(length)/count(*),2) as AVERAGE_LENGTH from length_value