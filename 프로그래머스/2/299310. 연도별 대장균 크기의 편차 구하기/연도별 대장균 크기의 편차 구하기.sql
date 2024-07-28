select year(DIFFERENTIATION_DATE) as YEAR,
(max(SIZE_OF_COLONY) over (partition by year(DIFFERENTIATION_DATE)) - size_of_colony) as YEAR_DEV, ID
from ecoli_data
order by year,year_dev