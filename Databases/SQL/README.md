# SQL

1. We can use alias by `as "col name"` with spaces.
2. Views are logical, materialized views are physical
3. We can use column alias in having for mysql
4. We can insert data and create tables from output of a query.
5. BEGIN TRANSACTION, COMMIT, ROLLBACK. Until commit is called, the changes are not visible to other transactions. We can rollback to undo the changes.
6. ` LIKE '%!%%' ESCAPE '!' ! is the escape character here. It gives words with % in them.
7. If you choose to have both aggregate and nonaggregate col‐
umns in the SELECT statement, you must include all nonag‐
gregate columns in the GROUP BY clause
8. TRIM(LEADING '!' FROM color) removes ! from color
9. We can use rollup, cube, grouping sets for grouping data. These provide addtional functionality

## Window Functions
1. `ROW_NUMBER() OVER (PARTITION BY gender ORDER BY babies DESC)` - `WINDOW_FUN OVER (PARTITION BY col1 ORDER BY col2)`
2. ROW_NUMBER() - Assigns a unique number to each row within the partition of a result set.
3. RANK() - Assigns a unique number to each distinct row within the partition of a result set. - 1,2,2,4
4. DENSE_RANK() - Assigns a unique number to each distinct row within the partition of a result set, leaving no gaps between the ranks. - 1,2,2,3
5. FIRST_VALUE(col) - Returns the first value in an ordered set of values. LAST_VALUE(col) - Returns the last value in an ordered set of values. NTH_VALUE(col, val) - Returns the nth value in an ordered set of values.
6. LAG(col, offset, default) - Returns the value of col from the row that is offset rows before the current row. LEAD(col, offset, default) - Returns the value of col from the row that is offset rows after the current row. Offset is by default 1. Default is the value to return if the offset goes beyond the bounds of the partition. Usually for the first row, the default is used.
7. We can use PRECEDING, FOLLOWING, UNBOUNDED, CURRENT ROW with window functions. - `SUM(sales) OVER (PARTITION BY name ORDER BY month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)`    
8. We can use RANGE instead of ROWS for window functions. RANGE is used for continuous values like dates. ROWS is used for discrete values like row numbers.
9. We can use window functions with aggregate functions. - `SUM(sales) OVER (PARTITION BY name ORDER BY month ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)`

## PIVOT
1. `SELECT * FROM fruits PIVOT (COUNT(id) FOR fruit IN ('strawberries', 'grapefruit', 'watermelon'));`. We could use case when for the same thing but pivot is more readable.

## Others
1. UNION - Combines the result sets of two or more SELECT statements into a single result set. The result set of a UNION operation contains all the rows that belong to all the SELECT statements in the UNION. The result set of a UNION is distinct.
2. UNION ALL - Combines the result sets of two or more SELECT statements into a single result set. The result set of a UNION ALL operation contains all the rows that belong to all the SELECT statements in the UNION ALL. The result set of a UNION ALL is not distinct.
3. INTERSECT - Combines the result sets of two or more SELECT statements into a single result set. The result set of an INTERSECT operation contains only the rows that appear in all the SELECT statements in the INTERSECT. The result set of an INTERSECT is distinct.
4. EXCEPT - Combines the result sets of two SELECT statements into a single result set. The result set of an EXCEPT operation contains only the rows that appear in the first SELECT statement but not in the second SELECT statement. The result set of an EXCEPT is distinct.
