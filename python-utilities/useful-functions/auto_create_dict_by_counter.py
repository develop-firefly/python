def auto_create_dict_by_counter() -> dict:
    '''
    Method to create a dictionary dataset automatically
    Argument to this method: None
    Keys are - Upper case Alpbabets
    Values are - Their count of occurrence
    '''
    my_str = UsefulUtils.get_upper_case_alphabets()
    # Return type is a dictionary
    return dict(collections.Counter(my_str))