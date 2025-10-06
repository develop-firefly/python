def db_get_column_names_of_table_by_sql_qry(self, _sql_query_or_sql_variable):
    '''
    Method to get the column names based on the sql query or sql variable
    Argument to this method is: SQL Query or Variable containing the SQL query
    '''
    with self.db_auto_connect.cursor(scrollable=True) as cursor:
        '''
        If you are fetching a fixed number of rows, start your tuning by setting arraysize to the number of expected
        rows, and set prefetchrows to one greater than this value. (Adding one removes the need for a round-trip to 
        check for end-of-fetch)
        '''
        cursor.arraysize = 1
        cursor.prefetchrows = 2
        # Execute the SQL Query or Variable containing the SQL query
        execute = cursor.execute(_sql_query_or_sql_variable)
        # Fetch the column names from cursor.description using list comprehension
        # 'description' attribute on a cursor holds the column names for the tables in question
        columns = [row[0] for row in execute.description]
    # return type of this method is a list
    return columns