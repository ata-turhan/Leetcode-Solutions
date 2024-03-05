SELECT COUNT(s.account_id) AS accounts_count 
FROM Subscriptions AS s 
LEFT JOIN streams AS st USING(account_id) 
WHERE (YEAR(start_date) <= 2021 AND YEAR(end_date) >= 2021) 
  AND (st.stream_date IS NULL OR YEAR(st.stream_date) != 2021);
