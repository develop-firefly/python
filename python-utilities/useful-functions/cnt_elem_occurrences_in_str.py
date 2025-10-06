def cnt_elem_occurrences_in_str(_inp_str : str) -> dict:
    '''
    Method to get occurrences of alphabets in string along with string
    Argument to this method: string
    '''
    # Return type is a dictionary where each alphabet of string is 'key' and their # of occurrences are values
    return dict(collections.Counter(_inp_str))