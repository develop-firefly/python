def get_unique_elems_from_str(_inp_str, case='str'):
    '''
    Method to get unique alphabets from input string
    Argument to this method: string or concatenated strings
    case user selected values to get output in specific data structure
    Valid values for case are:- str, list, tuple
    Default value for case : str
    '''
    # Following dictionary creates a case based logic
    conditional = { 'str'    : ''.join(_ for _ in collections.Counter(_inp_str).keys()),
                    'list'   : [_ for _ in collections.Counter(_inp_str).keys()],
                    'tuple'  : tuple(_ for _ in collections.Counter(_inp_str).keys())}
    # Return type is dependent on user selection of case
    return conditional.get(case)