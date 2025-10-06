def join_dicts_m2(*_dicts_iterables):
    '''
    Method to join multiple dictionaries to a single dictionary
    Argument to this method: Multiple Dictionaries as arguments (separated by comma)
    * takes care of the unpacking multiple dictionaries passed as arguments
    '''
    # Create an empty dictionary
    chained_dict = {}
    # Iterate over all the dictionaries in the unpacked list of dictionaries
    for _ in _dicts_iterables:
        # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
        chained_dict.update(_)
    # Return type is a dictionary
    return chained_dict