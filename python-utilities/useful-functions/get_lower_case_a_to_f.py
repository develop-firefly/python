def get_lower_case_a_to_f():
    '''
    Method to get lower case a through f
    Use of list comprehension with join
    Argument to this method: None
    '''
    # Return type is a string
    return ''.join(_ for _ in string.hexdigits if _.islower())