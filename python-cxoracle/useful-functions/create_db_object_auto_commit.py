def create_db_object_auto_commit(self, _sql_query_or_sql_variable):
    '''
    Method to Create a DB object and commit the changes
    Arguments to this Method: Sql Query or SQL Variable
    Note: Method verifies the existence of create keyword in the input statement
    '''
    try:
        # Connect to Database
        with self.db_auto_connect.cursor() as cursor:
            # Execute the query using the cursor
            cursor.execute(_sql_query_or_sql_variable)
        # Commit the DDL
        self.db_commit()
    # In Case Database Error occurs
    except cx_Oracle.DatabaseError as _errors:
        # Capture the errors in a variable
        _error, = _errors.args
        # The corresponding error code is loaded in to _error.code
        # Check if the encountered error is defined in the error map
        # If its defined, print the custom message based on the mapped key and value            
        if _error.code in CustomCxOracle._oracle_error_map.keys():
            # Following will be generated, if the Object already exists, if thats the case, simply ignore it
            if _error.code == 955:
                pass
            # Else, present the error code, so that it can be added to the code
            else:
                print(CustomCxOracle._oracle_error_map[_error.code])
        else:
            print('Method- create_db_object_auto_commit: Unmapped Errod Code, Please update error mapping for the class')