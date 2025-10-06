def cnt_occurrence_of_elem_in_chained_lists(*_lists_iterable, _element) -> int:
    '''
    Method to count occurrences of provided element in multiple lists
    Arguments to this method: Multiple lists as arguments (separated by comma), element to be counted
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # itertools.chain : joins the multiple lists into one
    chained_list = list(itertools.chain(*_lists_iterable))
    # chained_list.count(_element) counts the number of occurrences, if will be triggered only the result is not zero
    return chained_list.count(_element) if chained_list.count(_element) else 0