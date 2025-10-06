import itertools

def sum_elems_of_lists(*_inp_list):
    '''
    Method to join multiple lists into one list and sum all the digits
    Argument to this method: Multiple lists as arguments (separated by comma)
    * takes care of the unpacking multiple lists passed as arguments
    '''
    # itertools.chain(*_inp_list) : Joins all the lists into one list
    # Following List comprehension, filters only digits from the input list
    # Return type is an integer
    return sum(_ for _ in itertools.chain(*_inp_list) if str(_).isdigit())