 def join_dicts_m1(*_dicts_iterables):
     '''
     Method to join multiple dictionaries to a single dictionary
     Argument to this method: Multiple Dictionaries as arguments (separated by comma)
     * takes care of the unpacking multiple dictionaries passed as arguments
     '''
     # Using list comprehension to create a new dictionary with keys and values iterated from all the dictionaries in the unpacked list of dictionaries
     chained_dict = {k:v for d in _dicts_iterables for k,v in d.items()}
     # Return type is a dictionary
     return chained_dict