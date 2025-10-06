def merge_lists(*_lists_iterables):
    '''
    Method to join multiple lists into one list and keep only non-repeating values
    Argument to this method: Multiple lists as arguments (separated by comma)
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # itertools.chain : joins the multiple lists into one
    # set removes the duplicate entries from the list
    # list converts the unique set to a list
    merged_list = list(set(list(itertools.chain(*_lists_iterables))))
    # Return type is a list
    return merged_list