def cnt_occurrence_of_all_elems_in_chained_lists(*_lists_iterable) -> dict:
    '''
    Method to count occurrences of all elements in multiple lists
    Arguments to this method: Multiple lists as arguments (separated by comma)
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # itertools.chain : joins the multiple lists into one
    chained_list = list(itertools.chain(*_lists_iterable))
    # Count the Occurrence of each value in chained list and keep value as key and occurrence count as value
    # Return type is a dictionary
    return dict(collections.Counter(chained_list))