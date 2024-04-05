-- Calculate the peak calling hour for each city along with the number of calls during that hour
WITH PeakCallingHours AS (
    SELECT 
        city, 
        HOUR(call_time) AS peak_calling_hour, -- Extract the hour from the call_time
        COUNT(*) AS number_of_calls, -- Count the number of calls
        RANK() OVER (PARTITION BY city ORDER BY COUNT(*) DESC) AS rank_num -- Rank the calling hours based on the number of calls per city
    FROM 
        Calls 
    GROUP BY 
        city, HOUR(call_time) -- Group by city and hour
)

-- Select the peak calling hour for each city based on the highest number of calls
SELECT 
    city, 
    peak_calling_hour, -- Select the peak calling hour
    number_of_calls -- Select the number of calls during the peak calling hour
FROM 
    PeakCallingHours 
WHERE 
    rank_num = 1 -- Filter to include only the highest ranked (peak) calling hour for each city
ORDER BY 
    peak_calling_hour DESC, -- Order by peak calling hour in descending order
    city DESC; -- Then order by city in descending order
