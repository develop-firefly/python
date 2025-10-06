# Method to manually commit the sql
# Argument to this method: None
# Note: This is defined, since connection.auto commit is set to False by default, and I have kept it that way
def db_commit(self):
    self.db_auto_connect.commit()