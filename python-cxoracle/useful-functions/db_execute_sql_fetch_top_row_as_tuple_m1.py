# Method to fetch first row of sql output
# Argument to this method is: SQL Query or Variable containing the SQL query
# Note: Order of the result is driven by sql query
def db_execute_sql_fetch_top_row_as_tuples_m1(self, _sql_query_or_sql_variable):
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
        # Fetch only one of the items from the cursor in to results
        results = execute.fetchone()
    # return type of this method is a tuple
    return results