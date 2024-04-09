# Write your MySQL query statement below
with all_pairs as (
    select home_team_id as home, away_team_id as away, home_team_goals as hg, away_team_goals as ag  from matches
    union all
    select away_team_id as home, home_team_id as away, away_team_goals as hg, home_team_goals as ag from matches
),
all_stats as (
    select home, away, hg, ag, if(hg > ag, 3, 
    if(hg = ag, 1, 0)) as points from all_pairs
)

select t.team_name, count(m.home) as matches_played, sum(points) as points, sum(hg) as goal_for, sum(ag) as goal_against, (sum(hg)-sum(ag)) as goal_diff from teams as t join all_stats as m on t.team_id = m.home group by m.home order by points desc, goal_diff desc, team_name asc;