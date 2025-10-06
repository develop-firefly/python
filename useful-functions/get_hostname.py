# Import the platform package
import platform

def get_hostname():
    ''' Function to get the hostname of the machine
    The node method of platform module provides the hostname of the machine'''
    return platform.node()
    # Another way is to use the uname results named tuple
    # return platform.uname().node