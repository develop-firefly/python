def cnt_elem_occurrences_in_str_ordered_rslt(_inp_str, _sort_key='key', _sort_reversal=False) -> dict:
    '''
    Method to get occurrences of alphabets in string
    Sort the result dictionary by key or value
    Order the dictionary in asc or desc based on _sort_reversal
    Valid values for _sort_reversal are True / False
    Valid values for _sort_key are key / value
    Arguments to this method are: string, sorting key and sorting type        
    '''
    # collections.Counter will create a dictionary structure and get the count of each element of the string
    # element is the key and count is the value of that key
    result_set = collections.Counter(_inp_str)
    # Following if statement is triggered when user wants to sort the result by key
    # key can be any function, I have used the anonymous lambda function
    if _sort_key == 'key':
        return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_reversal)))
    # Following elif statement is triggered when user wants to sort the result by value of the key
    # key can be any function, I have used the anonymous lambda function
    elif _sort_key == 'value':
        return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_reversal)))