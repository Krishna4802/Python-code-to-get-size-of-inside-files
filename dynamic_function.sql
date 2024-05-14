CREATE OR ALTER PROCEDURE GetFieldsForTable
    @tableName NVARCHAR(100)
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);

    SET @sql = '
        SELECT field_name 
        FROM dbo.table_fields 
        WHERE parent_table = ''' + @tableName + '''
    ';

    EXEC sp_executesql @sql;
END;



--EXEC GetFieldsForTable 'Patient';
