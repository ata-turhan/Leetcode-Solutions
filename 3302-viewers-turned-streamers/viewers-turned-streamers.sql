with ranked_sessions as (
    select *, rank() over (partition by user_id order by session_start asc) as ranks from sessions
),
first_viewers as (
    select user_id from ranked_sessions where ranks = 1 and session_type = "Viewer"
)
select user_id, 
sum(if(session_type = "Streamer", 1, 0)) as sessions_count
 from sessions join first_viewers using(user_id) group by user_id having sessions_count > 0 order by 2 desc, 1 desc;
