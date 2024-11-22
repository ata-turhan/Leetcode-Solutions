WITH total_frequency AS (
    -- Calculate the total frequency
    SELECT SUM(frequency) AS total_freq
    FROM numbers
),
median_positions AS (
    -- Determine the positions of the median values
    SELECT 
        FLOOR((total_freq + 1) / 2) AS first_median_idx,
        CEIL((total_freq + 1) / 2) AS second_median_idx
    FROM total_frequency
),
cumulative_numbers AS (
    -- Compute cumulative frequency for each number
    SELECT 
        num, 
        SUM(frequency) OVER (ORDER BY num ASC) AS cum_freq
    FROM numbers
),
first_median_value AS (
    -- Find the first median value
    SELECT MIN(num) AS first_val
    FROM cumulative_numbers, median_positions
    WHERE cum_freq >= first_median_idx
),
second_median_value AS (
    -- Find the second median value
    SELECT MIN(num) AS second_val
    FROM cumulative_numbers, median_positions
    WHERE cum_freq >= second_median_idx
)
-- Calculate and round the median
SELECT 
    ROUND(
        (
            (SELECT first_val FROM first_median_value) + 
            (SELECT second_val FROM second_median_value)
        ) / 2.0, 1
    ) AS median;
