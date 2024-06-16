-- Main query to find all unique email domains ending with .com and their counts
SELECT 
    SUBSTRING_INDEX(email, '@', -1) AS email_domain,
    COUNT(*) AS count
FROM 
    Emails
WHERE 
    SUBSTRING_INDEX(email, '.', -1) = 'com'
GROUP BY 
    email_domain
ORDER BY 
    email_domain ASC;
