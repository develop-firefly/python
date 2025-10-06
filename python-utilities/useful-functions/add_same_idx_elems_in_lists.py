def add_same_idx_elems_in_lists(*_lists_iterable) -> list:
    '''
    Method to add elements at same index from multiple lists and create a new list
    Argument to this method: Multiple lists as arguments (separated by comma)
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # create an empty list to hold result of index wise additions
    final_result = []
    # Get the count of lists passed as arguments
    list_arg_cnt = UsefulUtils.get_arg_cnt(*_lists_iterable)
    # Identify the number of elements in biggest list
    biggest_list = [max(len(_) for _ in _lists_iterable)][0]
    # Depending on which variable is bigger, create a new dynamic condition for final addition
    # Creation of dynamic condition is needed since we will use it with zip(*_lists_iterable)
    if biggest_list < list_arg_cnt:
        dyn_condition = str(','.join('var'+str(_) for _ in range(1, list_arg_cnt+1)))
    else:
        dyn_condition = str(','.join('var'+str(_) for _ in range(1, biggest_list+1)))
    # Iterate over the lists from arguments and append the list which are shorter than the biggest list
    # If the iterated list is smaller than biggest list, append the list with 0 (int) to resize the list
    for _iter in _lists_iterable:
        if len(_iter) < dyn_condition.count(',') + 1:
            list_len_manager = (dyn_condition.count(',') + 1) - (len(_iter))
            for _extend in range(list_len_manager):
                _iter.append(0)
    # Iterate over elements starting at 0th index of all lists and add them
    # Once Addition is done for the 0th index, append the sum to final_result
    # This approach is more of a columnar addition
    for dyn_condition in zip(*_lists_iterable):
        # Define an Initial result variable and assign it with 0
        # This gets reset for every index position (vertically)
        init_res = 0
        # Iterate over new vertical list (0th, 1st, 2nd etc index positions) and add them
        for _ in dyn_condition:
            init_res += _
        # Append the sum of each columnar index position to final result
        final_result.append(init_res)
    # Return type is a list
    return final_result