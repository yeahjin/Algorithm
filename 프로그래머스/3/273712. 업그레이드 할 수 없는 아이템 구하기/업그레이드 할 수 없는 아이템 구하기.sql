-- 코드를 작성해주세요
select i.item_id, i.item_name, i.rarity from item_info as i
left join item_tree as t on t.PARENT_ITEM_ID = i.item_id
where t.item_id is null
order by i.item_id desc