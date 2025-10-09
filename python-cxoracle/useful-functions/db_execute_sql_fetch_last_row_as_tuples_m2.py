def db_execute_sql_fetch_last_row_as_tuples_m2(self, _sql_query_or_sql_variable):
    '''
    Method to fetch last row of sql output
    Argument to this method is: SQL Query or Variable containing the SQL query
    Note: Order of the result is driven by sql query
    '''
    # Open the cursor as 'with' so, it's automatically closed upon task completion
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
        '''
        Special Note:  Cursor.scroll(value=0, mode='relative')
        Scroll the cursor in the result set to a new position according to the mode.
        If mode is “relative” (the default value), the value is taken as an offset to the current position in the 
        result set. If set to “absolute”, value states an absolute target position. If set to “first”, the cursor 
        is positioned at the first row and if set to “last”, the cursor is set to the last row in the result set.

        An error is raised if the mode is “relative” or “absolute” and the scroll operation would position the 
        cursor outside of the result set.
        '''
        execute.scroll(mode='last')
        # Fetch only first item from the cursor in to results
        results = execute.fetchone()
    # return type of this method is a tuples
    return results