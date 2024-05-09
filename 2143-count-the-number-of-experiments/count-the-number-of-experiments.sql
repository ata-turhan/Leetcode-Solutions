-- Define platforms
WITH platforms AS (
    SELECT 'Android' AS platform
    UNION
    SELECT 'IOS' AS platform
    UNION
    SELECT 'Web' AS platform
),
-- Define experiment names
experiment_names AS (
    SELECT 'Reading' AS experiment_name 
    UNION
    SELECT 'Sports' AS experiment_name 
    UNION
    SELECT 'Programming' AS experiment_name 
),
-- Combine platforms and experiment names
platforms_and_experiment_names AS (
    SELECT * 
    FROM platforms
    CROSS JOIN experiment_names
),
-- Count the number of experiments for each platform-experiment combination
grpd_experiments AS (
    SELECT 
        platform, 
        experiment_name, 
        COUNT(experiment_id) AS num_experiments 
    FROM 
        Experiments 
    GROUP BY 
        platform, 
        experiment_name
)
-- Select and display the results
SELECT 
    pen.platform, 
    pen.experiment_name, 
    COALESCE(ge.num_experiments, 0) AS num_experiments 
FROM 
    platforms_and_experiment_names pen
LEFT JOIN 
    grpd_experiments ge 
    ON pen.platform = ge.platform AND pen.experiment_name = ge.experiment_name;
