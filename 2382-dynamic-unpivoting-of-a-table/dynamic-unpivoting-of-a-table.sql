CREATE PROCEDURE UnpivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;

    # Get the column names for the store columns
    SELECT GROUP_CONCAT(COLUMN_NAME)
    INTO @columns
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Products' AND COLUMN_NAME != 'product_id';

    # Generate the dynamic SQL
    SET @sql = CONCAT('SELECT product_id, store, price FROM (',
                      (SELECT GROUP_CONCAT(
                        CONCAT('SELECT product_id, \'', COLUMN_NAME, '\' as store, ', COLUMN_NAME, ' as price FROM Products WHERE ', COLUMN_NAME, ' IS NOT NULL')
                        SEPARATOR ' UNION ALL ')
                      FROM INFORMATION_SCHEMA.COLUMNS
                      WHERE TABLE_NAME = 'Products' AND COLUMN_NAME != 'product_id'),
                      ') as tmp');

    # Prepare and execute the dynamic SQL
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
