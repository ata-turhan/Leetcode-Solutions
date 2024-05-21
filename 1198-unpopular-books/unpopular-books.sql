-- Step 1: Filter books that have been available for at least one month
WITH FilteredBooks AS (
    SELECT
        book_id,
        name
    FROM
        Books
    WHERE
        available_from <= DATE_SUB('2019-06-23', INTERVAL 1 MONTH)
),

-- Step 2: Calculate the total quantity sold for each book in the last year
BookSalesLastYear AS (
    SELECT
        book_id,
        SUM(quantity) AS total_quantity
    FROM
        Orders
    WHERE
        dispatch_date BETWEEN DATE_SUB('2019-06-23', INTERVAL 1 YEAR) AND '2019-06-23'
    GROUP BY
        book_id
)

-- Step 3: Identify books that sold less than 10 copies in the last year
SELECT
    fb.book_id,
    fb.name
FROM
    FilteredBooks fb
LEFT JOIN
    BookSalesLastYear bsly ON fb.book_id = bsly.book_id
WHERE
    IFNULL(bsly.total_quantity, 0) < 10
ORDER BY
    fb.book_id;
