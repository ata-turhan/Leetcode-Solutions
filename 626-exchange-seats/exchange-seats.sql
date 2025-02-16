SELECT 
    CASE 
        WHEN s.id % 2 <> 0 AND s.id = (SELECT COUNT(*) FROM Seat) THEN s.id -- If last seat is odd, keep it unchanged
        WHEN s.id % 2 = 0 THEN s.id - 1 -- Swap even id with previous odd id
        ELSE s.id + 1 -- Swap odd id with next even id
    END AS id,
    student
FROM Seat AS s
ORDER BY id;
