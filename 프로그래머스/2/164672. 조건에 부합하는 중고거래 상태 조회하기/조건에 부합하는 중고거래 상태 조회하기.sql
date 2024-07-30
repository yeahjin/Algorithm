-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID,TITLE, PRICE,
case
    when STATUS = "SALE" then "판매중"
    when STATUS = "RESERVED" then "예약중"
    else "거래완료"
end as "STATUS"
from used_goods_board
where YEAR(created_date) = 2022 and MONTH(created_date)=10 and DAY(created_date) = 5
order by board_id desc