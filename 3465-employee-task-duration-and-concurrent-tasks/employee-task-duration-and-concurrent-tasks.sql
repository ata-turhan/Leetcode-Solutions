WITH TimeEvents AS (
    -- Step 1: Flatten task start and end times into a long format
    SELECT employee_id, start_time AS event_time, 1 AS event_type
    FROM Tasks
    UNION ALL
    SELECT employee_id, end_time AS event_time, -1 AS event_type
    FROM Tasks
),
ConcurrentTasks AS (
    -- Step 2: Calculate the number of concurrent tasks at any time for each employee
    SELECT 
        employee_id, 
        event_time, 
        event_type,
        SUM(event_type) OVER (PARTITION BY employee_id ORDER BY event_time) AS concurrent_tasks,
        LEAD(event_time) OVER (PARTITION BY employee_id ORDER BY event_time) AS next_event_time
    FROM TimeEvents
),
ValidTimeIntervals AS (
    -- Step 3: Calculate the duration between consecutive events where there is at least one active task
    SELECT 
        employee_id,
        event_time,
        next_event_time,
        TIMESTAMPDIFF(SECOND, event_time, next_event_time) / 3600 AS time_diff_hours,
        concurrent_tasks
    FROM ConcurrentTasks
    WHERE next_event_time IS NOT NULL
),
TaskDurations AS (
    -- Step 4: Total task hours for each employee, rounded down to the nearest hour
    SELECT 
        employee_id, 
        FLOOR(SUM(CASE WHEN concurrent_tasks > 0 THEN time_diff_hours ELSE 0 END)) AS total_task_hours
    FROM ValidTimeIntervals
    GROUP BY employee_id
),
MaxConcurrentTasks AS (
    -- Step 5: Find the maximum number of concurrent tasks for each employee
    SELECT 
        employee_id,
        MAX(concurrent_tasks) AS max_concurrent_tasks
    FROM ConcurrentTasks
    GROUP BY employee_id
)
-- Step 6: Combine the total task hours and max concurrent tasks
SELECT 
    td.employee_id,
    td.total_task_hours,
    mct.max_concurrent_tasks
FROM TaskDurations td
JOIN MaxConcurrentTasks mct ON td.employee_id = mct.employee_id
ORDER BY td.employee_id;
