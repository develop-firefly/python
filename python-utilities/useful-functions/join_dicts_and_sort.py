def join_dicts_and_sort(*_dicts_iterables, _sort_key='key', _sort_reversal=False):
    '''
    Method to join multiple dictionaries to a single dictionary and sort the new dictionary based on keys or value
    Ascending or Descending order
    Argument to this method: Multiple Dictionaries as arguments (separated by comma), sorting key and sorting type
    * takes care of the unpacking multiple dictionaries passed as arguments
    _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
    _sort_key='value' will sort the resulting dictionary by values in ascending order
    _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order
    '''
    # Create an empty dictionary
    merged_dict = {}
    # Iterate over all the dictionaries in the unpacked list of dictionaries
    for _ in _dicts_iterables:
        # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
        merged_dict |= _
    # Sort the updated dictionary based on keys in ascending order
    # usage of sorted method: sorted(iterable, key)
    # special note: key can be any user defined function as well
    # for sorting key, I am using the anonymous lambda function and item[0] refers to the dictionary keys
    if _sort_key == 'key':
        # Return type is a dictionary
        return dict(sorted(merged_dict.items(), key=lambda item:item[0], reverse=_sort_reversal))
    elif _sort_key == 'value':
        # Return type is a dictionary
        return dict(sorted(merged_dict.items(), key=lambda item:item[-1], reverse=_sort_reversal))