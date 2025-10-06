def db_execute_sql_fetch_top_row_as_set_m1(self, _sql_query_or_sql_variable):
    '''
    Method to fetch first row of sql output
    Argument to this method is: SQL Query or Variable containing the SQL query
    Note: Order of the result is driven by sql query
    Return type of this method is a set
    '''
    # Open the cursor as 'with' so, it's automatically closed upon task completion
    with self.db_auto_connect.cursor() as cursor:
        '''
        If you are fetching a fixed number of rows, start your tuning by setting arraysize to the number of expected 
        rows, and set prefetchrows to one greater than this value. (Adding one removes the need for a round-trip to 
        check for end-of-fetch)
        '''
        cursor.arraysize = 1
        cursor.prefetchrows = 2
        # Execute the SQL Query or Variable containing the SQL query
        execute = cursor.execute(_sql_query_or_sql_variable)
        '''
        Special Note:Cursor.rowfactory The rowfactory attribute of the Cursor object defines the method that will be
          called when retrieving the record. This attribute produces tuples by default. By overwriting this movement,
           it is possible to change the format of the record to another form.
        '''
        # Here we are changing the form from tuples to a set
        execute.rowfactory = lambda *args: set(args)
        # Fetch only one of the items from the cursor in to results
        results = execute.fetchone()
    # return type of this method is a set
    return results