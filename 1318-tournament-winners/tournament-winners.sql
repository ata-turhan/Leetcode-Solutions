with all_players as (
    select first_player as player_id, first_score as score from matches
    union all
    select second_player as player_id, second_score as score from matches
),
players_scores as (
    select player_id, sum(score) as total_score from all_players group by player_id
),
players_groups as (
    select ps.player_id, total_score, group_id from players_scores as ps join players as p on ps.player_id = p.player_id
),
players_ranks as (
    select group_id, player_id, rank() over ( partition by group_id order by total_score desc, player_id asc) as ranks from players_groups
)
select group_id, player_id from players_ranks where ranks = 1
