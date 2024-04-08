with all_pairs as (
    select user1_id, user2_id from Friendship
    union
    select user2_id, user1_id from Friendship
)


    select f1.user1_id, f1.user2_id, count(f3.user2_id) as common_friend from Friendship as f1
    join all_pairs as f2 on f1.user1_id = f2.user1_id and f1.user2_id != f2.user2_id join all_pairs as f3 on f1.user2_id = f3.user1_id and f2.user2_id = f3.user2_id group by f1.user1_id, f1.user2_id having common_friend >= 3; 