def db_sys_privileged_conn(self, **privileged_creds: dict):
    '''
    Method to create a privileged connection as SYSDBA
    Arguments to this method: Keyword Argument defined in db_conf as privileged_user
    '''
    self.client_version = cx_Oracle.clientversion()
    # username, password and dsn are read from the db_conf file
    # mode=cx_Oracle.SYSDBA is the key aspect for this privileged connection
    # Special note: Do not convert cx_Oracle.SYSDBA to str(cx_Oracle.SYSDBA), since cx_Oracle.SYSDBA results to 2
    # and cx_Oracle expects the value to be an integer
    sysdba_conn = cx_Oracle.connect(**privileged_creds)
    # return type of this method is a cx_Oracle connection object
    return sysdba_conn