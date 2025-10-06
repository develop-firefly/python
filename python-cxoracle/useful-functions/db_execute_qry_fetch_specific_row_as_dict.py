# Method to fetch specific row number of sql output
# Argument to this method is: SQL Query or Variable containing the SQL query and row number
# Note: Order of the result is driven by sql query
def db_execute_qry_fetch_specific_row_as_dict(self, _sql_query_or_sql_variable, _row_idx):
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
        '''
        Special Note:Cursor.rowfactory The rowfactory attribute of the Cursor object defines the method that will be
          called when retrieving the record. This attribute produces tuples by default. By overwriting this movement,
           it is possible to change the format of the record to another form.
        '''
        # Here we are changing the form from tuples to a dictionary
        execute.rowfactory = lambda *args: dict(zip(columns, args))
        '''
        Special Note:  Cursor.scroll(value=0, mode='relative')
        Scroll the cursor in the result set to a new position according to the mode.
        If mode is “relative” (the default value), the value is taken as an offset to the current position in the 
        result set. If set to “absolute”, value states an absolute target position. If set to “first”, the cursor 
        is positioned at the first row and if set to “last”, the cursor is set to the last row in the result set.

        An error is raised if the mode is “relative” or “absolute” and the scroll operation would position the 
        cursor outside of the result set.
        '''
        execute.scroll(_row_idx, mode='absolute')
        # Fetch only first item from the cursor in to results
        results = execute.fetchone()
    # return type of this method is a dict
    return results