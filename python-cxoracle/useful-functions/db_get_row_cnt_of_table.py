def db_get_row_cnt_of_table(self, table_name):
    '''
    Method to get the row count in a given table
    Argument to this method is: Name of the table
    Argument can be provided as standalone table name or with the schema.table_name
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
        '''
        Asserting SQL Object names taken as user input is a good security practice to avoid sql injection attack
        In following line:
        1. callfunc() : Is used to call a user defined or system provided function
        2. sys.dbms_assert.sql_object_name :- Is a Oracle DB provided function to validate if provided input is
            a valid sql object (A Table name in this case)
        3. Input to this function are two parameters (type) "String" and (object_name) "Table name"
        '''
        try:
            asserted_table_name = cursor.callfunc('sys.dbms_assert.sql_object_name', cx_Oracle.STRING, [table_name])
            # Pass the asserted table name as variable to _sql_query
            _sql_query = f'Select count(1) from {asserted_table_name}'
            # Fetch only first item from the cursor in to results
            execute = cursor.execute(_sql_query).fetchone()
            return execute[0]
        except cx_Oracle.DatabaseError as _errors:
            _error, = _errors.args
            if _error.code == 44002:
                return 'Invalid SQL Object Name, Please verify Object Name provided....'