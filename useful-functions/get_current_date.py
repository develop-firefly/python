# Import the datetime module
from datetime import datetime
def get_current_date():
    '''
    Method to get the current date
    Input: None
    Output: Current date in the format MM/DD/YYYY
    '''
    fmt = "%m/%d/%Y"
    return datetime.today().strftime(format=fmt)