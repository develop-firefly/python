# Method to execute a sql query or a query stored in a variable & fetch all results
# Argument to this method is: SQL Query or Variable containing the SQL query
# Note: Both Column names & Values are returned as a dictionary
def db_execute_sql_fetch_all_as_dict(self, _sql_query_or_sql_variable):
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
        # Fetch the column names from cursor.description using list comprehension
        # 'description' attribute on a cursor holds the column names for the tables in question
        columns = [row[0] for row in execute.description]
        '''
        Special Note:Cursor.rowfactory The rowfactory attribute of the Cursor object defines the method that will be
          called when retrieving the record. This attribute produces tuples by default. By overwriting this movement,
           it is possible to change the format of the record to another form.
        '''
        # Here we are changing the form from tuples to a dictionary
        # dict keys - Are the columns names in the table
        execute.rowfactory = lambda *args: dict(zip(columns, args))
        # FetchALL the rows from cursor in to results
        results = execute.fetchall()
    # return type of this method is dictionary
    return results