def get_upper_case_a_to_f():
    '''
    Method to get upper case A through F
    Use of list comprehension with join
    Argument to this method: None
    '''
    # Return type is a string
    return ''.join(_ for _ in string.hexdigits if _.isupper())