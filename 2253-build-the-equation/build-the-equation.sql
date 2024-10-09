WITH FormattedTerms AS (
    -- Format each term of the polynomial equation based on its power and factor
    SELECT 
        power,
        CASE
            WHEN power = 0 THEN
                -- Constant term: add '+' if factor is positive
                IF(SUBSTR(factor, 1, 1) = '-', factor, CONCAT('+', factor))
            WHEN power = 1 THEN
                -- Linear term: append 'X' to the factor
                IF(SUBSTR(factor, 1, 1) = '-', CONCAT(factor, 'X'), CONCAT('+', factor, 'X'))
            ELSE
                -- Higher-degree terms: append 'X^power' to the factor
                IF(SUBSTR(factor, 1, 1) = '-', CONCAT(factor, 'X^', power), CONCAT('+', factor, 'X^', power))
        END AS term
    FROM 
        terms
)
-- Concatenate all formatted terms in descending order of power to form the equation
SELECT 
    CONCAT(GROUP_CONCAT(term ORDER BY power DESC SEPARATOR ''), '=0') AS equation
FROM 
    FormattedTerms;
