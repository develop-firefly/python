def convert_set_to_dict(inp_set, starting_idx_position):
    '''
    Method to convert a set to a dictionary
    Input:1 - Iterable Sequence
    Input:2 - Starting Counter position
    Output: Dictionary with counter as key and iterable members as values
    '''
    # define an empty dictionary
    output_dict = dict()
    # Enumerate over the input set with a starting counter as provided by user
    for count, item in enumerate(inp_set,start=starting_idx_position):
        # Assign the counter as key and iterable members as values
        output_dict[count] = item
    return output_dict
