EXEC sp_MSforeachdb '
    USE [?];
    SELECT
        DB_NAME() AS DatabaseName,
        t.name AS TableName,
        c.name AS AttributeName
    FROM sys.tables AS t
    JOIN sys.columns AS c ON t.object_id = c.object_id;
';
