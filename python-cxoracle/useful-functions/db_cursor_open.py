def db_cursor_open(self):
    '''
    Method to create a cursor on the connected database
    Arguments to this method: None
    '''
    print('Cursor is manually opened, always remember to close it by calling db_cursor_close')
    return self.db_auto_connect.cursor()