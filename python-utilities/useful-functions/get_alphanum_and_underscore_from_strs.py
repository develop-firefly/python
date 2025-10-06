def get_alphanum_and_underscore_from_strs(*_inp_strs, delim=''):
    '''
    Method to extract aplhabets, numbers and underscore from given list of strings
    Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
    * takes care of the unpacking multiple strings passed as arguments
    Default value for delimiter is ''
    '''
    # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
    # Result of this method is a concatenated string
    # The Outer for loop simply iterates over all the elements of the concatenated string and filter only alphabets, numbers and underscore
    # These numerical values are then joined with user provided or default delimiter
    # Return type is string
    return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs) if _.isalnum() or _ in ('_')) 