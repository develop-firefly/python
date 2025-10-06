# Import the plaform package
import platform
# Method to get the architectural informartion of the machine
def get_architecture():
    ''' 
    Method to get the architectural informartion of the machine
    '''
    # The 'machine' method provides the architectural information of the local machine
    return platform.machine()
    # Another way to get the same information is via uname's named tuple result
    # return platform.uname().machine
