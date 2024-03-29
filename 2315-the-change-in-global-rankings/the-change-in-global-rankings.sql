WITH ranks AS (
    SELECT 
        team_id, 
        name, 
        CAST(rank() OVER (ORDER BY points DESC, name ASC) AS SIGNED) AS rank1,
        CAST(rank() OVER (ORDER BY (points + points_change) DESC, name ASC) AS SIGNED) AS rank2 
    FROM 
        teampoints AS t 
    JOIN 
        pointschange AS p USING (team_id)
)
SELECT 
    team_id, 
    name, 
    rank1 - rank2 AS rank_diff 
FROM 
    ranks;
