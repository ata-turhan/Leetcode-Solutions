SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month, 
    country, 
    COUNT(*) AS trans_count, 
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM transactions 
GROUP BY month, country;
