-- Step 1: Combine start and end times into a single dataset with an indicator for shift start (+1) or end (-1)
WITH ShiftChanges AS (
    SELECT 
        employee_id, 
        DATE(start_time) AS shift_date, 
        start_time AS change_time, 
        1 AS shift_change
    FROM EmployeeShifts
    UNION ALL
    SELECT 
        employee_id, 
        DATE(end_time) AS shift_date, 
        end_time AS change_time, 
        -1 AS shift_change
    FROM EmployeeShifts
),

-- Step 2: Calculate the number of concurrent shifts at any given time for each employee
ConcurrentShifts AS (
    SELECT 
        employee_id, 
        shift_date, 
        change_time, 
        SUM(shift_change) OVER (PARTITION BY employee_id, shift_date ORDER BY change_time) AS concurrent_count
    FROM ShiftChanges
),

-- Step 3: Find the maximum number of overlapping shifts for each employee
MaxOverlaps AS (
    SELECT 
        employee_id, 
        MAX(concurrent_count) AS max_overlapping_shifts
    FROM ConcurrentShifts
    GROUP BY employee_id
),

-- Step 4: Calculate the total duration of overlapping shifts for each employee
OverlapDurations AS (
    SELECT 
        e1.employee_id,
        SUM(
            GREATEST(
                TIMESTAMPDIFF(MINUTE, 
                    GREATEST(e1.start_time, e2.start_time), 
                    LEAST(e1.end_time, e2.end_time)
                ), 
                0
            )
        ) AS total_overlap_duration
    FROM EmployeeShifts e1
    JOIN EmployeeShifts e2 
        ON e1.employee_id = e2.employee_id 
        AND e1.start_time < e2.start_time
    WHERE 
        e1.end_time > e2.start_time
    GROUP BY 
        e1.employee_id
)

-- Step 5: Aggregate results and output the maximum overlaps and total overlap duration for each employee
SELECT 
    e.employee_id,
    COALESCE(m.max_overlapping_shifts, 1) AS max_overlapping_shifts, -- Maximum overlapping shifts for the employee
    COALESCE(o.total_overlap_duration, 0) AS total_overlap_duration  -- Total overlap duration in minutes
FROM 
    EmployeeShifts e
LEFT JOIN 
    MaxOverlaps m ON e.employee_id = m.employee_id
LEFT JOIN 
    OverlapDurations o ON e.employee_id = o.employee_id
GROUP BY
    e.employee_id
ORDER BY 
    e.employee_id;
