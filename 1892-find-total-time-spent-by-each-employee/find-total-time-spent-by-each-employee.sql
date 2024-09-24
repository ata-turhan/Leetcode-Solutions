-- Calculate the total time spent by each employee per day
SELECT 
    emp_id, 
    event_day AS "day", 
    SUM(out_time - in_time) AS total_time
FROM 
    employees
GROUP BY 
    emp_id, event_day;
