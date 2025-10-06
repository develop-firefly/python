def db_cursor_close(self):
    '''
    Method to manually close the cursor
    Arguments to this method: None
    '''
    return self.db_cursor_open().close()