-- Query to select first name, last name, city, and state by joining the person and address tables
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state  
FROM 
    person AS p
LEFT JOIN 
    address AS a ON p.personId = a.personId;
