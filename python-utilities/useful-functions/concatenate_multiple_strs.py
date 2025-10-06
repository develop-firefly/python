def concatenate_multiple_strs(*_inp_strs, case='original', delim='') -> str:
    '''
    Method to join multiple string arguments into one concatenated string
    Arguments to this method: Multiple strings as arguments (separated by comma), user provided delimiter
    * takes care of the unpacking multiple tuples passed as arguments
    If no delimiter is provided, <space> is used as default value
    '''
    # Return type is a string
    conditional = {'capitalize' : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))).capitalize(),
                   'lower'      : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))).lower(),
                   'original'   : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))),
                   'swapcase'   : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))).swapcase(),
                   'title'      : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))).title(),
                   'upper'      : delim.join(_ for _ in (''.join(_ for _ in _inp_strs))).upper()}
    return conditional.get(case)