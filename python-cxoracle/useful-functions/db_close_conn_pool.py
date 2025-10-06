def db_close_conn_pool(self):
    '''
    Method to close the connection pool
    Argument to this method:- None
    '''
    self.pool.close()