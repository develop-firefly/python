def are_strs_an_anagram_m1(_inp_str_1: str, _inp_str_2: str) -> bool:
    '''
    Method to check if two strings are anagrams
    Argument to this method: two strings
    '''
    # Return type is boolean
    return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False