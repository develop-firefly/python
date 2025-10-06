def get_first_val_by_max_occurence_in_joined_dicts(*_dicts_iterables):
    '''
    Method to return first value by max count of occurrence
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
    occurrence_dict = dict(collections.Counter(merged_dicts.values()))
    # Following will pick the first value from the dictionary with max count of occurence
    # If their are others, they will be ignored
    max_first_value = max(occurrence_dict, key=occurrence_dict.get)
    # Return type dependent on key
    return max_first_value