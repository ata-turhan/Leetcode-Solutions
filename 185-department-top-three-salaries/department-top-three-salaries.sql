SELECT
    d.name           AS department,
    e1.name          AS employee,
    e1.salary        AS salary
FROM
    employee AS e1
  INNER JOIN
    department AS d
    ON e1.departmentID = d.id
WHERE
    (
      SELECT
        COUNT(DISTINCT e2.salary)
      FROM
        employee AS e2
      WHERE
        e2.departmentID = e1.departmentID
        AND e2.salary > e1.salary
    ) < 3
ORDER BY
    d.name,
    e1.salary DESC;
