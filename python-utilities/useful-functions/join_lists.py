def join_lists(*_lists_iterables):
    '''
    Method to join multiple lists into one list
    Argument to this method: Multiple lists as arguments (separated by comma)
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # itertools.chain : joins the multiple lists into one
    chained_list = list(itertools.chain(*_lists_iterables))
    # Return type is a list
    return chained_list