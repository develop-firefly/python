# Import the plaform package
import platform
# Method to get the architectural informartion of the machine
def get_architecture():
    ''' 
    Method to get the architectural informartion of the machine
    Input: None
    Output: Architecture information as a string
    '''
    # The 'machine' method provides the architectural information of the local machine
    return platform.machine()
    # Another way to get the same information is via uname's named tuple result
    # return platform.uname().machine
