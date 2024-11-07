-- Combine first and second players' scores into one table
WITH combined_scores AS (
    SELECT first_player AS player_id, first_score AS score
    FROM matches
    UNION ALL
    SELECT second_player AS player_id, second_score AS score
    FROM matches
),

-- Calculate total scores for each player
player_total_scores AS (
    SELECT player_id, SUM(score) AS total_score
    FROM combined_scores
    GROUP BY player_id
),

-- Join players' total scores with their respective groups
player_group_scores AS (
    SELECT pts.player_id, pts.total_score, p.group_id
    FROM player_total_scores AS pts
    JOIN players AS p ON pts.player_id = p.player_id
),

-- Rank players within each group based on total score and player_id
grouped_ranking AS (
    SELECT group_id, player_id, 
           RANK() OVER (PARTITION BY group_id ORDER BY total_score DESC, player_id ASC) AS ranks
    FROM player_group_scores
)

-- Select the top-ranked players in each group
SELECT group_id, player_id
FROM grouped_ranking
WHERE ranks = 1;
