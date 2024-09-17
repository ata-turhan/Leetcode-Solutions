WITH bull_files AS (
    SELECT DISTINCT file_name
    FROM files
    WHERE LOWER(content) LIKE '% bull %'
),
bear_files AS (
    SELECT DISTINCT file_name
    FROM files
    WHERE LOWER(content) LIKE '% bear %'
)

SELECT 'bull' AS word, COUNT(*) AS count
FROM bull_files
UNION ALL
SELECT 'bear', COUNT(*)
FROM bear_files;
