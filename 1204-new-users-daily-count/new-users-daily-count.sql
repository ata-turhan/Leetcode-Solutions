-- Step 1: Get the earliest login date for each user
WITH FirstLogin AS (
    SELECT
        user_id,
        MIN(activity_date) AS first_login_date
    FROM
        Traffic
    WHERE
        activity = 'login'
    GROUP BY
        user_id
),

-- Step 2: Filter the first login dates to be within the last 90 days from the given date
FilteredLogins AS (
    SELECT
        first_login_date
    FROM
        FirstLogin
    WHERE
        first_login_date BETWEEN DATE_SUB('2019-06-30', INTERVAL 90 DAY) AND '2019-06-30'
)

-- Step 3: Count the number of first logins per day
SELECT
    first_login_date AS login_date,
    COUNT(*) AS user_count
FROM
    FilteredLogins
GROUP BY
    first_login_date
ORDER BY
    first_login_date;
