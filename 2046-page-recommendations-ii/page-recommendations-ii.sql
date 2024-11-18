with all_friends as (
    select * from friendship
    union all
    select user2_id, user1_id from friendship
)
select af.user1_id as user_id, l1.page_id, count(af.user2_id) as friends_likes  
from all_friends as af 
left join likes as l1 on af.user2_id = l1.user_id 
left join likes as l2 on af.user1_id = l2.user_id and l1.page_id = l2.page_id
where l2.page_id is null
group by af.user1_id, l1.page_id
