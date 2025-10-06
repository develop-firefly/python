def db_print_tabular_data(self, _sql_query_or_sql_variable):
    '''
    Method to print data in tabular format for a given query
    Argument to this method: SQL Query or Variable containing the SQL query
    '''
    # Open the cursor as 'with' so, it's automatically closed upon task completion
    with self.db_auto_connect.cursor(scrollable=True) as cursor:
        # 'arraysize' attribute of cursor is a performance tuning parameter
        # For queries returning unknown number of rows (basically large) or production set up
        # It's advisable to leave the 'prefetchrows' attribute to its default value of 2 and only adjust arraysize
        # I have kept the arraysize = 500 (same as in sql developer config), but this number should change
        # based on what kind of production load are we dealing with
        # Additional Info on Tuning is here:- https://cx-oracle.readthedocs.io/en/latest/user_guide/tuning.html?
        cursor.arraysize = 500
        # Execute the SQL Query or Variable containing the SQL query
        execute = cursor.execute(_sql_query_or_sql_variable)
        # Get the column names of the table by using another method in the same class
        columns = self.db_get_column_names_of_table_by_sql_qry(_sql_query_or_sql_variable)
        # FetchALL the rows from cursor in to results
        results = execute.fetchall()
        # return type of this method is tabular data
        # results = holds the data
        # headers = holds the column names
        # tablefmt = 'psql' is the core of format
        # valid values for tablefmt are:- psql, grid, pipe, html
        return tabulate(results, headers=columns, tablefmt='psql')        