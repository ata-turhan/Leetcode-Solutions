-- CTE to calculate left max height for each position
WITH LeftMax AS (
    SELECT 
        id, 
        height,
        MAX(height) OVER (ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS left_max
    FROM 
        Heights
),

-- CTE to calculate right max height for each position
RightMax AS (
    SELECT 
        id, 
        height,
        MAX(height) OVER (ORDER BY id DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS right_max
    FROM 
        Heights
),

-- CTE to join the left max and right max heights with the original heights
WaterLevels AS (
    SELECT 
        l.id,
        l.height,
        l.left_max,
        r.right_max,
        LEAST(l.left_max, r.right_max) AS water_level
    FROM 
        LeftMax l
    JOIN 
        RightMax r ON l.id = r.id
)

-- Main query to calculate the total trapped water
SELECT 
    SUM(GREATEST(water_level - height, 0)) AS total_trapped_water
FROM 
    WaterLevels;
