# Write your MySQL query statement below
select sum(b.apple_count + ifnull(c.apple_count, 0)) as apple_count,
sum(b.orange_count  + ifnull(c.orange_count, 0)) as orange_count
from boxes as b left join chests as c using(chest_id)