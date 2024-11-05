WITH all_calls AS (
    -- This CTE generates a combined view of all calls from both caller to recipient and recipient to caller
    SELECT caller_id, recipient_id, call_time, DATE(call_time) AS call_date FROM calls
    UNION ALL
    SELECT recipient_id AS caller_id, caller_id AS recipient_id, call_time, DATE(call_time) AS call_date FROM calls
),
first_and_last_calls AS (
    -- Get the first and last recipient per caller and date, ensuring last_value captures the last row by setting a window frame
    SELECT 
        caller_id,
        FIRST_VALUE(recipient_id) OVER (PARTITION BY caller_id, call_date ORDER BY call_time ASC) AS first_called,
        LAST_VALUE(recipient_id) OVER (PARTITION BY caller_id, call_date ORDER BY call_time ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_called
    FROM all_calls 
)

-- Find callers who called the same person first and last in a day
SELECT DISTINCT caller_id as user_id
FROM first_and_last_calls 
WHERE first_called = last_called;
