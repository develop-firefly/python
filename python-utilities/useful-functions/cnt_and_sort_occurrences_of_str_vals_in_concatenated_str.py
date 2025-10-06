def cnt_and_sort_occurrences_of_str_vals_in_concatenated_str(*_iterables, _sort_key='key', _sort_reversal=False) -> dict:
    '''
    Method to count occurrences of all elements in multiple strings
    Argument to this method: Multiple strings as arguments (separated by comma), sorting key and sorting type
    * takes care of the unpacking multiple strings passed as arguments
    _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
    _sort_key='value' will sort the resulting dictionary by values in ascending order
    _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order        
    '''
    # Use list comprehension to join the string without a space / delimiter
    joined_string = ''.join(_ for _ in _iterables)
    # Count the Occurrence of each element in joined string and keep element as key and occurrence count as value
    occurrence_dict = dict(collections.Counter(joined_string))
    # Return type is a dictionary
    if _sort_key == 'key':
        return dict(sorted(occurrence_dict.items(), key = lambda item:item[0], reverse=_sort_reversal))
    elif _sort_key == 'value':
        return dict(sorted(occurrence_dict.items(), key = lambda item:item[-1], reverse=_sort_reversal))