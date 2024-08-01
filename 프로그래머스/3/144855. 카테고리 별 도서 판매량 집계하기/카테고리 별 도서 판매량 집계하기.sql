-- 코드를 입력하세요
SELECT CATEGORY,sum(sales) as TOTAL_SALES from book
left join book_sales using(book_id)
where YEAR(SALES_DATE) = 2022 and MONTH(sales_date) = 1
group by category
order by category