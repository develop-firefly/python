def get_vals_by_min_occurrence_in_joined_dicts(*_dicts_iterables):
    '''
    Method to return Values by min count of occurrence
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
    # List comprehension to get the list of values with min occurrence in dictionaries
    # Using list comprehension, since their may be mutliple values having same occurence count as min count
    min_value = [k for k, v in occurrence_dict.items() if v == min(occurrence_dict.values())]
    # Return type is a List
    return min_value