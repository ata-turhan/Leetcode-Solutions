-- CTE to calculate the answer rates for each question and rank them
WITH answer_rates AS (
    SELECT 
        question_id, 
        ROW_NUMBER() OVER (ORDER BY SUM(action = 'answer') / SUM(action = 'show') DESC, question_id ASC) AS rn 
    FROM 
        surveylog 
    GROUP BY 
        question_id
)

-- Main query to find the question with the highest answer rate
SELECT 
    question_id AS survey_log 
FROM 
    answer_rates 
WHERE 
    rn = 1 
    AND question_id IS NOT NULL;
