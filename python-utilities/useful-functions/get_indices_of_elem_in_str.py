def get_indices_of_elem_in_str(*_inp_str, _elem, return_type='list'):
    '''
    Method to get Indices of a given element in provided strings
    Arguments to this method: Multiple Strings and Element for which we need indices, return type selected by user
    * takes care of the unpacking multiple dictionaries passed as arguments
    Default value for return_type is <list>
    '''
    # Call the method concatenate_multiple_strs to join the provided strings
    concatenated_str = UsefulUtils.concatenate_multiple_strs(*_inp_str)
    # Following dictionary creates a case based logic
    # Data type of values is changed based on the key selection by user
    # Iterate over the elements concatenated string
    # Using Enumerate and List Comprehension with Conditional statement, get the <list> of Indices of matched values
    # Return type is dependent on user selection
    # _inp_str.__class__ : Enforces the datatype of list comprehension to be same as Input <tuple>
    # *_inp_str : Is a list of tuples when unpacked
    conditional = { 'list' : [key for key, val in enumerate(concatenated_str) if val == _elem],
                    'tuple' : _inp_str.__class__(key for key, val in enumerate(concatenated_str) if val == _elem)}
    return conditional.get(return_type)