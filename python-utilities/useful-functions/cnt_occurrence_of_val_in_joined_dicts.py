def cnt_occurrence_of_val_in_joined_dicts(*_dicts_iterables, _value) -> dict:
    '''
    Method to count occurrences of specific value in multiple dictionaries
    Arguments to this method: Multiple dictionaries as arguments (separated by comma), _value to count occurence for
    * takes care of the unpacking multiple dictionaries passed as arguments
    '''
    # Create an empty dictionary
    merged_dicts = {}
    # Iterate over all the dictionaries in the unpacked list of dictionaries
    for _ in _dicts_iterables:
        # Update the empty dictionary with keys and Values from unpacked list of dictionaries
        merged_dicts |= _
    # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
    occurrence_dict = dict(collections.Counter(merged_dicts.values()))
    # Return type is an integer
    try:
        # If the searched value exists in the dictionary, return its count of occurence
        return occurrence_dict[_value]
        # If the searched value does not exist in dictionary, return integer 0
    except KeyError:
        return 0