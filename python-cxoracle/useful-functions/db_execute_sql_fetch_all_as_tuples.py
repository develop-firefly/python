def db_execute_sql_fetch_all_as_tuples(self, _sql_query_or_sql_variable):
    '''
    Method to execute a sql query or a query stored in a variable & fetch all results
    Argument to this method is: SQL Query or Variable containing the SQL query
    Return type of this method is tuple (default behavior)
    '''
    # Open the cursor as 'with' so, it's automatically closed upon task completion
    with self.db_auto_connect.cursor() as cursor:
        # 'arraysize' attribute of cursor is a performance tuning parameter
        # For queries returning unknown number of rows (basically large) or production set up
        # It's advisable to leave the 'prefetchrows' attribute to its default value of 2 and only adjust arraysize
        # I have kept the arraysize = 500 (same as in sql developer config), but this number should change
        # based on what kind of production load are we dealing with
        # Additional Info on Tuning is here:- https://cx-oracle.readthedocs.io/en/latest/user_guide/tuning.html?
        cursor.arraysize = 500
        # Execute the SQL Query or Variable containing the SQL query
        execute = cursor.execute(_sql_query_or_sql_variable)
        # FetchALL the rows from cursor in to results
        results = execute.fetchall()
    # return type of this method is tuple (default behavior)
    return results