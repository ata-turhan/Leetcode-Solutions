-- Common Table Expression to create pairs of teams with their respective goals from matches table
WITH all_pairs AS (
    -- Selecting home and away teams along with their goals
    SELECT home_team_id AS home, away_team_id AS away, home_team_goals AS hg, away_team_goals AS ag FROM matches
    UNION ALL
    -- Union to consider both home and away teams
    SELECT away_team_id AS home, home_team_id AS away, away_team_goals AS hg, home_team_goals AS ag FROM matches
),

-- Common Table Expression to calculate points based on match results
all_stats AS (
    -- Assigning points based on match results (3 points for win, 1 point for draw, 0 points for loss)
    SELECT home, away, hg, ag, IF(hg > ag, 3, IF(hg = ag, 1, 0)) AS points FROM all_pairs
)

-- Main query to retrieve team statistics
SELECT 
    t.team_name, -- Team name
    COUNT(m.home) AS matches_played, -- Total matches played
    SUM(points) AS points, -- Total points earned
    SUM(hg) AS goal_for, -- Total goals scored
    SUM(ag) AS goal_against, -- Total goals conceded
    (SUM(hg) - SUM(ag)) AS goal_diff -- Goal difference
FROM 
    teams AS t -- Teams table
JOIN 
    all_stats AS m ON t.team_id = m.home -- Joining with the all_stats table on home team ID
GROUP BY 
    m.home -- Grouping by home team ID
ORDER BY 
    points DESC, -- Ordering by points in descending order
    goal_diff DESC, -- Then by goal difference in descending order
    team_name ASC; -- Finally by team name in ascending order
