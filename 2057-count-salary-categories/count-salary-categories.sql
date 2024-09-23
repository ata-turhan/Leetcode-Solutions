-- Select the count of accounts in the "Low Salary" category
SELECT "Low Salary" AS category,
       SUM(income < 20000) AS accounts_count
  FROM Accounts

UNION

-- Select the count of accounts in the "Average Salary" category
SELECT "Average Salary" AS category,
       SUM(income BETWEEN 20000 AND 50000) AS accounts_count
  FROM Accounts

UNION

-- Select the count of accounts in the "High Salary" category
SELECT "High Salary" AS category,
       SUM(income > 50000) AS accounts_count
  FROM Accounts;
