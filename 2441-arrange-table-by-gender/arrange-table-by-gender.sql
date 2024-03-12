# Write your MySQL query statement below
with ranked as (select user_id, gender, rank() over (partition by gender order by user_id) + (case when gender = "female" then 0.1 when gender = "other" then 0.2 else 0.3 end) as ranks from genders)

select user_id, gender from ranked order by ranks