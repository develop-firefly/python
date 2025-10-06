# Method to execute any sql as sysdba
# Argument to this method is: SQL Query or Variable containing the SQL query
def db_execute_sql_as_sysdba(self, _sql_query_or_sql_variable):
    # Open the cursor as 'with' so, it's automatically closed upon task completion
    with self.db_sys_privileged_conn().cursor() as sysdba_cursor:
        # Execute the SQL Query or Variable containing the SQL query as SYSDBA
        sysdba_execute = sysdba_cursor.execute(_sql_query_or_sql_variable)
        # Fetch ALL the rows from cursor in to results
        results = sysdba_execute.fetchall()
    # return type of this method is tuple (default behavior)
    return results