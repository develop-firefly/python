def chk_db_object_existence(self, db_schema_name, db_obj_name):
    '''
    Method to check Existence of a Database Object
    Arguments to this Method: schema name and object name
    '''
    # Prepare the query to check the object in Oracle Database
    _existence_qry = f"Select owner, object_name, object_type from all_objects where 1=1 and owner='{db_schema_name}' and object_name='{db_obj_name}'"
    # Connect to Database
    with self.db_auto_connect.cursor() as cursor:
        # Use Ternary operator, validate the bool return type of the query
        # fetchall() is needed to pull the results of the existence query in a list
        # If the list is empty, then the table does not exists
        return ((False, True) [bool(len(cursor.execute(_existence_qry).fetchall()))])