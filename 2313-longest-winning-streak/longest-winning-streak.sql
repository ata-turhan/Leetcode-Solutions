WITH match_results AS (
    -- Calculate if a match is a win (1) or not (0) for each player
    SELECT 
        player_id,
        match_day,
        result,
        IF(result = 'Win', 1, 0) AS is_win
    FROM matches
),
match_ordered AS (
    -- Assign a row number to each match per player based on the match day to track the sequence
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day ASC) AS match_row
    FROM match_results
),
match_with_cumsum AS (
    -- Calculate the cumulative sum of wins per player ordered by match day to track win progress
    SELECT 
        *,
        SUM(is_win) OVER (PARTITION BY player_id ORDER BY match_day ASC) AS win_cumsum
    FROM match_ordered
),
win_groups AS (
    -- Group wins into streaks by subtracting cumulative sum from row number to assign unique group ids for each streak
    SELECT 
        *,
        match_row - win_cumsum AS win_group_id
    FROM match_with_cumsum
    WHERE is_win = 1  -- Only consider matches where the result is a win
),
win_streaks AS (
    -- Count the length of each winning streak by grouping by player and win_group_id
    SELECT 
        player_id,
        win_group_id,
        COUNT(*) AS streak_length
    FROM win_groups
    GROUP BY player_id, win_group_id
),
player_win_count AS (
    -- Calculate the total number of wins for each player to identify players with zero wins
    SELECT 
        player_id,
        SUM(is_win) AS total_wins
    FROM match_results
    GROUP BY player_id
),
zero_win_players AS (
    -- Identify players who have zero wins and assign them a longest streak of 0
    SELECT 
        player_id, 
        0 AS longest_streak
    FROM player_win_count
    WHERE total_wins = 0
),
non_zero_win_players AS (
    -- Identify players with at least one win and find their longest win streak
    SELECT 
        player_id,
        MAX(streak_length) AS longest_streak
    FROM win_streaks
    GROUP BY player_id
)
-- Combine the results: players with zero wins and players with their longest winning streaks
SELECT 
    player_id, 
    longest_streak
FROM non_zero_win_players

UNION ALL

SELECT 
    player_id, 
    longest_streak
FROM zero_win_players

ORDER BY player_id;
