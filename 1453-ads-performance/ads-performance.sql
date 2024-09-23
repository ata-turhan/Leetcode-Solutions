SELECT
    ad_id,
    ROUND(
        IFNULL(
            (SUM(action = 'Clicked') / (SUM(action = 'Clicked') + SUM(action = 'Viewed'))) * 100,
            0
        ), 
        2
    ) AS ctr
FROM
    Ads
GROUP BY
    ad_id
ORDER BY
    ctr DESC,
    ad_id ASC;
