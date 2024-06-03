with ranks as (
    select seller_id, count(distinct item_id) as num_items, rank() over ( order by count(distinct item_id) desc ) as rank_num from orders as o join items as i using(item_id) join users as u using(seller_id) where favorite_brand != item_brand group by seller_id
)

select seller_id, num_items from ranks where rank_num = 1;