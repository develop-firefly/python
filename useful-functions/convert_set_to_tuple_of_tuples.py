def convert_set_to_tuple_of_tuples(inp_set, starting_idx_position, increment_by):
    '''
    Method to convert a set to a tuple of tuples
    Input:1 - Iterable Sequence
    Input:2 - Starting Counter position
    Input:3 - Increment the Counter by this number
    '''
    # Validate if the "increment by" is an integer
    assert type(increment_by) == int, "Increment By MUST be an integer"
    # Enumerate over the input set with a starting counter as provided by user
    for count, item in enumerate(inp_set, start=starting_idx_position):
        # Create a generator object using yield to create the tuple members
        yield starting_idx_position, item
        # increment counter position by this number
        starting_idx_position += increment_by

# Note: The final Print statement will determine the output datatype
# Example:  print(tuple(convert_set_to_tuple_of_tuples(inp_set, 2,  3))) : Will generate a tuple of tuples        