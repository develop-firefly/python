def assign_same_val_to_all_keys(*_keys : list, _value) -> dict:
    '''
    Method to assign same values to provided keys and create a dictionary
    Arguments to this method: _keys as multiple list of elements, _value as any value
    '''
    # itertools.repeat : repeats the passed value seamlessly
    # zip : ties the keys and value together together
    # itertools.chain(*_keys) : Joins all lists to form a single list
    # Return type is a dictionary
    return dict(zip(itertools.chain(*_keys), itertools.repeat(_value)))