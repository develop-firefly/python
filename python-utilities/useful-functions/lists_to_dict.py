def lists_to_dict(key_list, val_list):
    '''
    Method to create a dictionary based on two lists
    Argument to this method: Two lists
    Elements of 1st list are treated as 'Keys' and 2nd list as 'Values'
    '''
    # Return type is a dictionary
    return dict(zip(key_list, val_list))