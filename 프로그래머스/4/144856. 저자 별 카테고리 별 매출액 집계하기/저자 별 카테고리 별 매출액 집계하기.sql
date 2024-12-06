with a as(SELECT book_id, sum(sales) as total_sales from book_sales
where date_format(sales_date, "%Y-%m") = "2022-01"
group by book_id),

b as (select author_id, category, sum(price*total_sales) as total_sales from book as b
left join a on a.book_id = b.book_id
group by category, author_id)

select b.author_id, author_name,b.category, b.total_sales from b
left join author as c on c.author_id = b.author_id
order by author_id, category desc