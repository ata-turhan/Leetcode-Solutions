WITH SpendingClassification AS (
    -- Classify each user's spending by date and platform
    SELECT 
        spend_date,
        user_id,
        SUM(CASE WHEN platform = 'mobile' THEN amount ELSE 0 END) AS mobile_amount,
        SUM(CASE WHEN platform = 'desktop' THEN amount ELSE 0 END) AS desktop_amount
    FROM 
        spending
    GROUP BY 
        spend_date, user_id
),
SpendingType AS (
    -- Determine the type of spending: 'both', 'mobile', or 'desktop'
    SELECT 
        spend_date,
        user_id,
        CASE 
            WHEN mobile_amount > 0 AND desktop_amount > 0 THEN 'both'
            WHEN mobile_amount > 0 THEN 'mobile'
            WHEN desktop_amount > 0 THEN 'desktop'
        END AS spending_type,
        (mobile_amount + desktop_amount) AS total_amount
    FROM 
        SpendingClassification
),
PlatformSummary AS (
    -- Aggregate total amount and total users for each platform on each date
    SELECT 
        spend_date,
        spending_type AS platform,
        SUM(total_amount) AS total_amount,
        COUNT(DISTINCT user_id) AS total_users
    FROM 
        SpendingType
    GROUP BY 
        spend_date, spending_type
),
AllPlatforms AS (
    -- Create all combinations of spend_date and platform for completeness
    SELECT 
        DISTINCT spend_date, platform_type AS platform
    FROM 
        spending
    CROSS JOIN 
        (SELECT 'mobile' AS platform_type UNION ALL SELECT 'desktop' UNION ALL SELECT 'both') AS platforms
)
-- Combine the summaries with all platforms for a complete result
SELECT 
    ap.spend_date,
    ap.platform,
    COALESCE(ps.total_amount, 0) AS total_amount,
    COALESCE(ps.total_users, 0) AS total_users
FROM 
    AllPlatforms ap
LEFT JOIN 
    PlatformSummary ps ON ap.spend_date = ps.spend_date AND ap.platform = ps.platform
ORDER BY 
    ap.spend_date, 
    FIELD(ap.platform, 'mobile', 'desktop', 'both');
