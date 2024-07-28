-- 코드를 입력하세요
with max_product as (
select max(PRICE) as max_price from food_product
)

SELECT * from food_product
where price = (select * from max_product)