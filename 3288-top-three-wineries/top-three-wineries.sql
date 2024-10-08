WITH WineryPoints AS (
    -- Calculate the total points for each winery within each country
    SELECT 
        country, 
        winery, 
        SUM(points) AS total_points 
    FROM 
        wineries 
    GROUP BY 
        country, winery
),
WineryRankings AS (
    -- Assign a rank to each winery within its country based on the total points (descending order)
    SELECT 
        country, 
        winery, 
        total_points, 
        RANK() OVER (PARTITION BY country ORDER BY total_points DESC, winery ASC) AS winery_rank 
    FROM 
        WineryPoints
)
-- Select the top, second, and third ranked wineries for each country
SELECT 
    wr1.country, 
    CONCAT(wr1.winery, " (", wr1.total_points, ")") AS top_winery,
    IFNULL(CONCAT(wr2.winery, " (", wr2.total_points, ")"), "No second winery") AS second_winery,
    IFNULL(CONCAT(wr3.winery, " (", wr3.total_points, ")"), "No third winery") AS third_winery
FROM 
    WineryRankings AS wr1 
    -- Join with second-ranked winery
    LEFT JOIN WineryRankings AS wr2 
    ON wr1.country = wr2.country 
    AND wr2.winery_rank = 2
    -- Join with third-ranked winery
    LEFT JOIN WineryRankings AS wr3 
    ON wr1.country = wr3.country 
    AND wr3.winery_rank = 3
WHERE 
    wr1.winery_rank = 1 -- Focus on the top-ranked winery for each country
