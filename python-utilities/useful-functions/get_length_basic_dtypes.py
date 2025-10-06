def get_length_basic_dtypes(_inp):
    '''
    Method to get length of input:
    This method is limited to basic data types (int, str, list, tuple, dict)
    Argument to this method: Input Variable
    Utilizes the length_hint function from the operator module
    '''
    # Return type is an Integer
    return operator.length_hint(str(_inp)) if type(_inp) is int else operator.length_hint(_inp)