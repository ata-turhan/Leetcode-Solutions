-- Calculate maximum fraud scores for each state and store in a common table expression (CTE) for reusability
WITH max_fraud_scores AS (
    SELECT 
        state, 
        MAX(fraud_score) AS max_fraud_score 
    FROM 
        fraud 
    GROUP BY 
        state
)

-- Retrieve policy information along with the corresponding maximum fraud score for each state
SELECT 
    f.policy_id, 
    f.state, 
    f.fraud_score 
FROM 
    fraud f
JOIN 
    max_fraud_scores mfs ON f.state = mfs.state AND f.fraud_score = mfs.max_fraud_score
ORDER BY 
    f.state ASC, 
    f.fraud_score DESC, 
    f.policy_id ASC;
