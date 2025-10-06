def merge_tuples(*_tuple_iterables):
    '''
    Method to join multiple tuples arguments into one tuple and remove duplicate elements from result tuple
    Arguments to this method: Multiple tuples as arguments (separated by comma)
    * takes care of the unpacking multiple tuples passed as arguments
    '''
    # itertools.chain : joins multiple tuples in to one
    # set : removes the duplicate elements from the result
    joined_tuple = tuple(set(itertools.chain(*_tuple_iterables)))
    # Return type is a tuple
    return joined_tuple