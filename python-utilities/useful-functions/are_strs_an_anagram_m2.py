def are_strs_an_anagram_m2(_inp_str_1: str, _inp_str_2: str) -> bool:
    '''
    Method to check if two strings are anagrams
    Argument to this method: two strings
    '''        
    # Return type is boolean
    # Utilizes Ternary Operator Approach
    # In Ternary Operators: False Boolean is written first and True Boolean is written next
    return ( (False, True) [collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2)])