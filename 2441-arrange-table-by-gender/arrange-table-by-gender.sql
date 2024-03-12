SELECT 
    user_id, 
    gender 
FROM 
    genders 
ORDER BY 
    RANK() OVER (PARTITION BY gender ORDER BY user_id) + 
        (CASE 
            WHEN gender = 'female' THEN 0.1 
            WHEN gender = 'other' THEN 0.2 
            ELSE 0.3 
        END);
