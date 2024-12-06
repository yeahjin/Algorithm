-- 코드를 입력하세요
SELECT a.author_id, a.author_name, b.category, sum(sales*price) as total_sales from book_sales as bs
join book as b on b.book_id = bs.book_id
join author as a on a.author_id = b.author_id
where date_format(bs.sales_date, "%Y-%m") = "2022-01"
group by a.author_id, b.category
order by a.author_id asc, b.category desc;