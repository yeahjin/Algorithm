-- 코드를 입력하세요
with a as (SELECT product_id,sum(sales_amount) as s from offline_sale
group by product_id)

select product_code, p.price * s as sales from product as p
left join a using(product_id)
where s is not null
order by sales desc, p.product_code