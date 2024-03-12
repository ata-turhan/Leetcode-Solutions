WITH ranked AS (
    SELECT 
        user_id, 
        gender, 
        RANK() OVER (PARTITION BY gender ORDER BY user_id) + 
        (CASE 
            WHEN gender = 'female' THEN 0.1 
            WHEN gender = 'other' THEN 0.2 
            ELSE 0.3 
        END) AS ranks 
    FROM 
        genders
)

SELECT 
    user_id, 
    gender 
FROM 
    ranked 
ORDER BY 
    ranks;
