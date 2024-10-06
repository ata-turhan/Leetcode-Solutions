WITH salary_employee AS (
    -- Join salary and employee tables and extract the pay month
    SELECT 
        employee_id, 
        department_id, 
        amount, 
        DATE_FORMAT(pay_date, '%Y-%m') AS pay_month 
    FROM 
        salary 
    JOIN 
        employee USING(employee_id)
),
company_salaries AS (
    -- Calculate the average company salary for each month
    SELECT 
        AVG(amount) AS avg_comp, 
        pay_month 
    FROM 
        salary_employee 
    GROUP BY 
        pay_month
),
department_salaries AS (
    -- Calculate the average salary for each department in each month
    SELECT 
        AVG(amount) AS avg_dep, 
        pay_month, 
        department_id 
    FROM 
        salary_employee 
    GROUP BY 
        pay_month, 
        department_id
)
-- Compare department salary with the company average for each month
SELECT 
    pay_month, 
    department_id, 
    (CASE 
        WHEN avg_dep = avg_comp THEN "same"
        WHEN avg_dep > avg_comp THEN "higher"
        ELSE "lower"
    END) AS comparison
FROM 
    department_salaries 
JOIN 
    company_salaries USING(pay_month);
