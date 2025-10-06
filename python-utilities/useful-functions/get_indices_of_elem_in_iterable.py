def get_indices_of_elem_in_iterable(*_inp_iterable, _elem, return_type='list'):
    '''
    Method to get Indices of a given element in provided lists
    Arguments to this method: Multiple lists and Element for which we need indices, return type selected by user
    * takes care of the unpacking multiple dictionaries passed as arguments
    Default value for return_type is <list>
    '''
    # Call the method join_lists to join the provided lists
    chained_iterable = UsefulUtils.join_lists(*_inp_iterable)
    # Following dictionary creates a case based logic
    # Data type of values is changed based on the key selection by user
    # Iterate over the elements joined lists
    # Using Enumerate and List Comprehension with Conditional statement, get the <list> of Indices of matched values
    # Return type is dependent on user selection
    # _inp_iterable.__class__ : Enforces the datatype of list comprehension to be same as Input <tuple>
    # *_inp_iterable : Is a list of tuples when unpacked
    conditional = { 'list' : [key for key, val in enumerate(chained_iterable) if val == _elem],
                    'tuple' : _inp_iterable.__class__(key for key, val in enumerate(chained_iterable) if val == _elem)}
    return conditional.get(return_type)