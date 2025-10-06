def partition_iterables_to_iterable_of_n_elems(*_inp_lists, num_of_elems=3, case='list_of_lists'):
    '''
    Method to join multiple iterables to single iterable and then split that iterable in to elements of n length
    Argument to this method: Multiple lists as arguments (separated by comma), number of elements to use for splitting
    case user selected values to get output in specific data structure
    Valid values for case are:- list_of_lists, list_of_tuples, tuple_of_lists, tuple_of_tuples
    Default value for case : list_of_lists
    '''
    # itertools.chain(*_inp_list) will join all the lists in to one list
    chained_iterable = list(itertools.chain(*_inp_lists))
    
    # Iternal Method to return the new iterable split based on user provided number of elements
    # Argument to this method: Joined list from above and number of elements to use for splitting
    def core_logic(chained_iterable, num_of_elems):
        # Create an empty list
        new_iterable = []
        # Iterate over all elements of the joined list based on the range and use the step function of list data strcuture
        # num_of_elems is passed as the step value
        for _ in range(0, len(chained_iterable), num_of_elems):
            # Append the empty list based on the slicing of list
            new_iterable.append(chained_iterable[_:_+num_of_elems])
        # Return type of this method is list
        return new_iterable
    # Following dictionary creates a case based logic
    # Valid values are the keys and value is the function call with parameters to core_logic method
    # Data type of values is changed based on the key selection by user
    driver = {'list_of_lists'   : core_logic(chained_iterable, num_of_elems),
              'list_of_tuples'  : core_logic(tuple(chained_iterable), num_of_elems),
              'tuple_of_lists'  : tuple(core_logic(chained_iterable, num_of_elems)),
              'tuple_of_tuples' : tuple(core_logic(tuple(chained_iterable), num_of_elems))}
    # Return type is dependent on the case provided by user
    return driver.get(case)