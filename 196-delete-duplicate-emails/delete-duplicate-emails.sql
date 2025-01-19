-- Delete duplicate email entries while keeping the record with the smallest id
DELETE p2
FROM Person p1
JOIN Person p2
  ON p1.Email = p2.Email  -- Match records with the same email
  AND p1.Id < p2.Id;       -- Ensure we are deleting the record with the larger id
