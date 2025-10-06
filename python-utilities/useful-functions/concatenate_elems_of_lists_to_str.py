def concatenate_elems_of_lists_to_str(*_inp_list, case='original') -> str:
    '''
    Method to concatenate elements of multiple lists
    Arguments to this method: Multiple lists as arguments (separated by comma), case of the result
    * takes care of the unpacking multiple lists passed as arguments
    Valid values for case are: 'capitalize', 'lower', 'original', 'swapcase', 'title', 'upper'
    Default value of case is : original        
    '''
    # Following is a dictionary with case values as keys and corresponding list comprehensions as their evaluated values
    # itertools.chain(*_inp_list) will join all the lists in to one list
    # Each element of the list will be joined using space as delimiter and then string function based on user selection are applied
    conditional = {'capitalize' : ' '.join(_ for _ in itertools.chain(*_inp_list)).capitalize(),
                   'lower'      : ' '.join(_ for _ in itertools.chain(*_inp_list)).lower(),
                   'original'   : ' '.join(_ for _ in itertools.chain(*_inp_list)),
                   'swapcase'   : ' '.join(_ for _ in itertools.chain(*_inp_list)).swapcase(),
                   'title'      : ' '.join(_ for _ in itertools.chain(*_inp_list)).title(),
                   'upper'      : ' '.join(_ for _ in itertools.chain(*_inp_list)).upper()}
    # Return type is a string
    return conditional.get(case)