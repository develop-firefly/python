def cnt_occurrence_of_all_vals_in_joined_dicts(*_dicts_iterables) -> dict:
    '''
    Method to count occurrences of all values in multiple dictionaries
    Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    * takes care of the unpacking multiple dictionaries passed as arguments
    '''
    # Create an empty dictionary
    merged_dicts = {}
    # Iterate over all the dictionaries in the unpacked list of dictionaries
    for _ in _dicts_iterables:
        # Update the empty dictionary with keys and Values from unpacked list of dictionaries
        merged_dicts |= _
    # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
    # Return type is a dictionary
    return dict(collections.Counter(merged_dicts.values()))