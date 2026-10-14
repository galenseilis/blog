-- Select the database you want to use.
USE [<DB_NAME>];

-- Set the table you want to summarize.
DECLARE @tabname NVARCHAR(50);
SET @tabname '<TABLE_NAME>';

-- Leave this alone (unless you want to change what is returned)
SELECT
    c.name 'column_name',
    t.Name 'data_type',
    c.max_length 'max_length',
    c.precision,
    c.scale,
    c.is_nullable,
    ISNULL(i.is_primary_key, 0) 'primary_key'
FROM
    sys.columns c
INNER JOIN
    sys.types t ON c.user_type_id = t.user_type_id
LEFT OUTER JOIN
    sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE
    c.object_id = OBJECT_ID(@tabname);
