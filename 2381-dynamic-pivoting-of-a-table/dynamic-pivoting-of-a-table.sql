CREATE PROCEDURE PivotProducts()
BEGIN
    -- Step 1: Override GROUP_CONCAT length to prevent truncation of the query
    SET SESSION group_concat_max_len = 1000000;

    -- Step 2: Prepare the case statements for the pivoted columns
    SET @case_stmt = NULL;

    -- Step 3: Dynamically generate the case statements for each distinct store
    SELECT GROUP_CONCAT(DISTINCT CONCAT('SUM(CASE WHEN store = "', store, '" THEN price END) AS `', store, '`'))
    INTO @case_stmt
    FROM Products;

    -- Step 4: Construct the full dynamic query
    SET @sql_query = CONCAT('SELECT product_id, ', @case_stmt, ' FROM Products GROUP BY product_id ORDER BY product_id');

    -- Step 5: Execute the dynamic query
    PREPARE final_sql_query FROM @sql_query;
    EXECUTE final_sql_query;
    DEALLOCATE PREPARE final_sql_query;
END;
