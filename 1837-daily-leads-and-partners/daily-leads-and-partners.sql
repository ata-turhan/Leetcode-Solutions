-- Query to select date_id, make_name, unique lead counts, and unique partner counts
SELECT 
    date_id, 
    make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads,  -- Count distinct leads
    COUNT(DISTINCT partner_id) AS unique_partners  -- Count distinct partners
FROM 
    DailySales
-- Group the result by date_id and make_name
GROUP BY 
    date_id, 
    make_name;
