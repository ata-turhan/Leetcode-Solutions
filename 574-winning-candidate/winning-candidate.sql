-- Calculate the number of votes received by each candidate and store in a common table expression (CTE) for reusability
WITH vote_counts AS (
    SELECT 
        candidateId, 
        COUNT(id) AS counts -- Calculate the number of votes for each candidate
    FROM 
        vote 
    GROUP BY 
        candidateId
),
-- Identify the candidate(s) with the maximum number of votes
max_voted_candidateId AS (
    SELECT 
        candidateId -- Select the candidate ID(s) with the maximum vote count
    FROM 
        vote_counts 
    WHERE 
        counts = (SELECT MAX(counts) FROM vote_counts) -- Subquery to find the maximum vote count
)

-- Retrieve the name(s) of the candidate(s) with the maximum number of votes
SELECT 
    c.name -- Select the name of the candidate
FROM 
    candidate c -- Alias for the candidate table
JOIN 
    max_voted_candidateId mvc ON c.id = mvc.candidateId; -- Join the candidate table with the candidate(s) having the maximum vote count
