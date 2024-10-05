with inactive_sellers as (
    select user_id, "no" as "2nd_item_fav_brand" from orders right join users on orders.seller_id = users.user_id group by user_id having count(order_id) < 2
),
active_sellers as (
        select * from orders where seller_id not in (select user_id from inactive_sellers)
),
active_sellers_rank as (
    select *, row_number() over (partition by seller_id order by order_date asc) as ranks from active_sellers
)
select asr.seller_id, if(u.favorite_brand = i.item_brand, "yes", "no" ) as "2nd_item_fav_brand" from active_sellers_rank as asr left join users as u on asr.seller_id = u.user_id left join items as i on asr.item_id = i.item_id where ranks = 2
union all
select * from inactive_sellers
