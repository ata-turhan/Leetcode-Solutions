with matches_win as (
    select *, if(result="Win", 1, 0) as is_win from matches
),
matches_rn as (
    select *, row_number() over(partition by player_id order by match_day asc) as rn  from matches_win
),
matches_cumsum as (
    select *, sum(is_win) over(partition by player_id order by match_day asc)  as cumsum from matches_rn
),
matches_groups as (
    select *, rn - cumsum as group_id from matches_cumsum where is_win = 1
),
matches_group_counts as (
    select player_id, group_id, count(group_id) as group_count from matches_groups group by player_id, group_id
),
win_counts as (
    select player_id, sum(is_win) as win_count from matches_win group by player_id
),
zero_wins as (
    select player_id, 0 as "longest_streak" from win_counts where win_count = 0
),
nonzero_wins as (
    select player_id, max(group_count) as longest_streak from matches_group_counts group by player_id
)
select * from nonzero_wins
union all
select * from zero_wins
