# Method to close the connection to database
# Argument to this method: None
# Note: This method is manual, since I did not use auto object / connection termination using 'with'
def db_disconnect(self):
    self.db_auto_connect.close()