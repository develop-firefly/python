# Import string module
import string
# Import collections module
import collections
# Import Itertools module
import itertools
# Import Operator module
import operator


# Class definitions should use CamelCase convention based on pep-8 guidelines
class UsefulUtils:

    def add_same_idx_elems_in_lists(*_lists_iterable: list) -> list:
        '''
        Method to add elements at same index from multiple lists and create a new list
        Argument to this method: Multiple lists as arguments (separated by comma)
        * takes care of the unpacking multiple lists passed as arguments
        '''
        # create an empty list to hold result of index wise additions
        final_result = []
        # Get the count of lists passed as arguments
        list_arg_cnt = UsefulUtils.get_arg_cnt(*_lists_iterable)
        # Identify the number of elements in biggest list
        biggest_list = [max(len(_) for _ in _lists_iterable)][0]
        # Depending on which variable is bigger, create a new dynamic condition for final addition
        # Creation of dynamic condition is needed since we will use it with zip(*_lists_iterable)
        if biggest_list < list_arg_cnt:
            dyn_condition = str(','.join('var'+str(_) for _ in range(1, list_arg_cnt+1)))
        else:
            dyn_condition = str(','.join('var'+str(_) for _ in range(1, biggest_list+1)))
        # Iterate over the lists from arguments and append the list which are shorter than the biggest list
        # If the iterated list is smaller than biggest list, append the list with 0 (int) to resize the list
        for _iter in _lists_iterable:
            if len(_iter) < dyn_condition.count(',') + 1:
                list_len_manager = (dyn_condition.count(',') + 1) - (len(_iter))
                for _extend in range(list_len_manager):
                    _iter.append(0)
        # Iterate over elements starting at 0th index of all lists and add them
        # Once Addition is done for the 0th index, append the sum to final_result
        # This approach is more of a columnar addition
        for dyn_condition in zip(*_lists_iterable):
            # Define an Initial result variable and assign it with 0
            # This gets reset for every index position (vertically)
            init_res = 0
            # Iterate over new vertical list (0th, 1st, 2nd etc index positions) and add them
            for _ in dyn_condition:
                init_res += _
            # Append the sum of each columnar index position to final result
            final_result.append(init_res)
        # Return type is a list
        return final_result

    def are_strs_an_anagram_m1(_inp_str_1: str, _inp_str_2: str) -> bool:
        '''
        Method to check if two strings are anagrams
        Argument to this method: two strings
        '''
        # Return type is boolean
        return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False
    
    def are_strs_an_anagram_m2(_inp_str_1: str, _inp_str_2: str) -> bool:
        '''
        Method to check if two strings are anagrams
        Argument to this method: two strings
        '''        
        # Return type is boolean
        # Utilizes Ternary Operator Approach
        # In Ternary Operators: False Boolean is written first and True Boolean is written next
        return ( (False, True) [collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2)])    

    def assign_same_val_to_all_keys(*_keys : list, _value) -> dict:
        '''
        Method to assign same values to provided keys and create a dictionary
        Arguments to this method: _keys as multiple list of elements, _value as any value
        '''
        # itertools.repeat : repeats the passed value seamlessly
        # zip : ties the keys and value together together
        # itertools.chain(*_keys) : Joins all lists to form a single list
        # Return type is a dictionary
        return dict(zip(itertools.chain(*_keys), itertools.repeat(_value)))

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

    def chk_if_str_empty_m1(_inp_str) -> bool:
        '''
        Method to check if given string is empty or not
        Argument to this method: string
        '''
        # Return type is boolean
        return True if not _inp_str else False

    def chk_if_str_empty_m2(_inp_str) -> bool:
        '''
        Method to check if given string is empty or not
        Argument to this method: string
        '''
        # Return type is boolean
        # Utilizes Ternary Operator Approach
        # In Ternary Operators: False Boolean is written first and True Boolean is written next
        return ((False, True) [not _inp_str])

    def cnt_and_sort_occurrences_of_str_vals_in_concatenated_str(*_iterables, _sort_key='key', _sort_reversal=False) -> dict:
        '''
        Method to count occurrences of all elements in multiple strings
        Argument to this method: Multiple strings as arguments (separated by comma), sorting key and sorting type
        * takes care of the unpacking multiple strings passed as arguments
        _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
        _sort_key='value' will sort the resulting dictionary by values in ascending order
        _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order        
        '''
        # Use list comprehension to join the string without a space / delimiter
        joined_string = ''.join(_ for _ in _iterables)
        # Count the Occurrence of each element in joined string and keep element as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(joined_string))
        # Return type is a dictionary
        if _sort_key == 'key':
            return dict(sorted(occurrence_dict.items(), key = lambda item:item[0], reverse=_sort_reversal))
        elif _sort_key == 'value':
            return dict(sorted(occurrence_dict.items(), key = lambda item:item[-1], reverse=_sort_reversal))
    
    def cnt_elem_occurrences_in_str_ordered_rslt(_inp_str, _sort_key='key', _sort_reversal=False) -> dict:
        '''
        Method to get occurrences of alphabets in string
        Sort the result dictionary by key or value
        Order the dictionary in asc or desc based on _sort_reversal
        Valid values for _sort_reversal are True / False
        Valid values for _sort_key are key / value
        Arguments to this method are: string, sorting key and sorting type        
        '''
        # collections.Counter will create a dictionary structure and get the count of each element of the string
        # element is the key and count is the value of that key
        result_set = collections.Counter(_inp_str)
        # Following if statement is triggered when user wants to sort the result by key
        # key can be any function, I have used the anonymous lambda function
        if _sort_key == 'key':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_reversal)))
        # Following elif statement is triggered when user wants to sort the result by value of the key
        # key can be any function, I have used the anonymous lambda function
        elif _sort_key == 'value':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_reversal)))

    def cnt_elem_occurrences_in_str(_inp_str : str) -> dict:
        '''
        Method to get occurrences of alphabets in string along with string
        Argument to this method: string
        '''
        # Return type is a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return dict(collections.Counter(_inp_str))

    def cnt_occurrence_of_all_elems_in_chained_lists(*_lists_iterable) -> dict:
        '''
        Method to count occurrences of all elements in multiple lists
        Arguments to this method: Multiple lists as arguments (separated by comma)
        * takes care of the unpacking multiple lists passed as arguments
        '''
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # Count the Occurrence of each value in chained list and keep value as key and occurrence count as value
        # Return type is a dictionary
        return dict(collections.Counter(chained_list))

    def cnt_occurrence_of_all_vals_in_joined_dicts(*_dicts_iterables) -> dict:
        '''
        Method to count occurrences of all values in multiple dictionaries
        Arguments to this method: Multiple dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        # Return type is a dictionary
        return dict(collections.Counter(merged_dicts.values()))

    def cnt_occurrence_of_elem_in_chained_lists(*_lists_iterable, _element) -> int:
        '''
        Method to count occurrences of provided element in multiple lists
        Arguments to this method: Multiple lists as arguments (separated by comma), element to be counted
        * takes care of the unpacking multiple lists passed as arguments
        '''
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # chained_list.count(_element) counts the number of occurrences, if will be triggered only the result is not zero
        return chained_list.count(_element) if chained_list.count(_element) else 0
        
    def cnt_occurrence_of_val_in_joined_dicts(*_dicts_iterables, _value) -> dict:
        '''
        Method to count occurrences of specific value in multiple dictionaries
        Arguments to this method: Multiple dictionaries as arguments (separated by comma), _value to count occurence for
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Return type is an integer
        try:
            # If the searched value exists in the dictionary, return its count of occurence
            return occurrence_dict[_value]
            # If the searched value does not exist in dictionary, return integer 0
        except KeyError:
            return 0

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

    def get_alphabets_from_strs(*_inp_strs, delim='') -> str:
        '''
        Method to extract alphabets from given list of strings
        Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
        * takes care of the unpacking multiple strings passed as arguments
        Default value for delimiter is ''
        '''
        # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
        # Result of this method is a concatenated string
        # The Outer for loop simply iterates over all the elements of the concatenated string and filter only aplhabetical values
        # These alphabetical values are then joined with user provided or default delimiter
        # Return type is string
        return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs)  if _.isalpha())

    def get_alphabets():
        '''
        Method to get both lower case and upper case letters (a through Z)
        Argument to this method: None
        '''
        # Return type is a string
        return string.ascii_letters

    def get_alphanum_and_underscore_from_strs(*_inp_strs, delim=''):
        '''
        Method to extract aplhabets, numbers and underscore from given list of strings
        Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
        * takes care of the unpacking multiple strings passed as arguments
        Default value for delimiter is ''
        '''
        # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
        # Result of this method is a concatenated string
        # The Outer for loop simply iterates over all the elements of the concatenated string and filter only alphabets, numbers and underscore
        # These numerical values are then joined with user provided or default delimiter
        # Return type is string
        return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs) if _.isalnum() or _ in ('_')) 

    def get_alphanum_from_strs(*_inp_strs, delim=''):
        '''
        Method to extract aplhabets and numbers from given list of strings
        Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
        * takes care of the unpacking multiple strings passed as arguments
        Default value for delimiter is ''
        '''
        # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
        # Result of this method is a concatenated string
        # The Outer for loop simply iterates over all the elements of the concatenated string and filter only alphabets and numbers
        # These numerical values are then joined with user provided or default delimiter
        # Return type is string
        return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs) if _.isalnum())

    def get_arg_cnt(*_arg):
        '''
        Method to get the number of arguments
        Arguments are passed as a list, separated by comma
        '''
        # Return type is an integer
        return len(_arg)

    def get_digits_from_strs(*_inp_strs, delim=''):
        '''
        Method to extract digits from given list of strings
        Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
        * takes care of the unpacking multiple strings passed as arguments
        Default value for delimiter is ''
        '''
        # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
        # Result of this method is a concatenated string
        # The Outer for loop simply iterates over all the elements of the concatenated string and filter only digits
        # These numerical values are then joined with user provided or default delimiter
        # Return type is string
        return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs) if _.isdigit())     

    def get_first_val_by_max_occurence_in_joined_dicts(*_dicts_iterables):
        '''
        Method to return first value by max count of occurrence
        Arguments to this method: Multiple dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Following will pick the first value from the dictionary with max count of occurence
        # If their are others, they will be ignored
        max_first_value = max(occurrence_dict, key=occurrence_dict.get)
        # Return type dependent on key
        return max_first_value

    def get_indices_of_elem_in_iterable(*_inp_iterable, _elem, return_type='list'):
        '''
        Method to get Indices of a given element in provided lists
        Arguments to this method: Multiple lists and Element for which we need indices, return type selected by user
        * takes care of the unpacking multiple dictionaries passed as arguments
        Default value for return_type is <list>
        '''
        # Call the method join_lists to join the provided lists
        chained_iterable = UsefulUtils.join_lists(*_inp_iterable)
        # Following dictionary creates a case based logic
        # Data type of values is changed based on the key selection by user
        # Iterate over the elements joined lists
        # Using Enumerate and List Comprehension with Conditional statement, get the <list> of Indices of matched values
        # Return type is dependent on user selection
        # _inp_iterable.__class__ : Enforces the datatype of list comprehension to be same as Input <tuple>
        # *_inp_iterable : Is a list of tuples when unpacked
        conditional = { 'list' : [key for key, val in enumerate(chained_iterable) if val == _elem],
                        'tuple' : _inp_iterable.__class__(key for key, val in enumerate(chained_iterable) if val == _elem)}
        return conditional.get(return_type)

    def get_indices_of_elem_in_str(*_inp_str, _elem, return_type='list'):
        '''
        Method to get Indices of a given element in provided strings
        Arguments to this method: Multiple Strings and Element for which we need indices, return type selected by user
        * takes care of the unpacking multiple dictionaries passed as arguments
        Default value for return_type is <list>
        '''
        # Call the method concatenate_multiple_strs to join the provided strings
        concatenated_str = UsefulUtils.concatenate_multiple_strs(*_inp_str)
        # Following dictionary creates a case based logic
        # Data type of values is changed based on the key selection by user
        # Iterate over the elements concatenated string
        # Using Enumerate and List Comprehension with Conditional statement, get the <list> of Indices of matched values
        # Return type is dependent on user selection
        # _inp_str.__class__ : Enforces the datatype of list comprehension to be same as Input <tuple>
        # *_inp_str : Is a list of tuples when unpacked
        conditional = { 'list' : [key for key, val in enumerate(concatenated_str) if val == _elem],
                        'tuple' : _inp_str.__class__(key for key, val in enumerate(concatenated_str) if val == _elem)}
        return conditional.get(return_type)

    def get_last_val_by_max_occurence_in_joined_dicts(*_dicts_iterables):
        '''
        Method to return last value by max count of occurrence
        Arguments to this method: Multiple dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Following will pick the last value from the dictionary with max count of occurrence
        # If their are others, they will be ignored
        max_last_value = max(reversed(occurrence_dict), key=occurrence_dict.get)
        # Return type dependent on key
        return max_last_value

    def get_length_basic_dtypes(_inp):
        '''
        Method to get length of input:
        This method is limited to basic data types (int, str, list, tuple, dict)
        Argument to this method: Input Variable
        Utilizes the length_hint function from the operator module
        '''
        # Return type is an Integer
        return operator.length_hint(str(_inp)) if type(_inp) is int else operator.length_hint(_inp)

    def get_lower_case_a_to_f():
        '''
        Method to get lower case a through f
        Use of list comprehension with join
        Argument to this method: None
        '''
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.islower())

    def get_lower_case_alphabets():
        '''
        Method to get only lower case letters (a through z)
        Argument to this method: None
        '''
        # Return type is a string
        return string.ascii_lowercase

    def get_punctuations_from_strs(*_inp_strs, delim=''):
        '''
        Method to extract special characters from given list of strings
        Argument to this method: Multiple strings as arguments (separated by comma), user provided delimiter
        * takes care of the unpacking multiple strings passed as arguments
        Default value for delimiter is ''
        '''
        # Internal for loop is calling the 'concatenate_multiple_strs' method in the same class
        # Result of this method is a concatenated string
        # The Outer for loop simply iterates over all the elements of the concatenated string and filter only digits
        # These numerical values are then joined with user provided or default delimiter
        # Return type is string
        return delim.join(_ for _ in UsefulUtils.concatenate_multiple_strs(*_inp_strs) if not _.isalnum())  

    def get_special_chars():
        '''
        Method to get special characters
        Argument to this method: None
        '''
        # Return type is a string
        # returns: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return string.punctuation

    def get_str_0_7():
        '''
        Method to get numbers 0 through 7 as string
        Argument to this method: None
        '''
        # Return type is a string
        return string.octdigits

    def get_str_0_9():
        '''
        Method to get numbers 0 through 9 as string
        Argument to this method: None
        '''
        # Return type is a string
        return string.digits
       
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

    def get_upper_case_a_to_f():
        '''
        Method to get upper case A through F
        Use of list comprehension with join
        Argument to this method: None
        '''
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.isupper())

    def get_upper_case_alphabets():
        '''
        Method to get only upper case letters (A through Z)
        Argument to this method: None
        '''
        # Return type is a string
        return string.ascii_uppercase

    def get_vals_by_max_occurrence_in_joined_dicts(*_dicts_iterables):
        '''
        Method to return Values by max count of occurrence
        Arguments to this method: Multiple dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # List comprehension to get the list of values with max occurrence in dictionaries
        # Using list comprehension, since their may be mutliple values having same occurrence count as max count
        max_value = [k for k, v in occurrence_dict.items() if v == max(occurrence_dict.values())]
        # Return type is a List
        return max_value

    def get_vals_by_min_occurrence_in_joined_dicts(*_dicts_iterables):
        '''
        Method to return Values by min count of occurrence
        Arguments to this method: Multiple dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value            
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # List comprehension to get the list of values with min occurrence in dictionaries
        # Using list comprehension, since their may be mutliple values having same occurence count as min count
        min_value = [k for k, v in occurrence_dict.items() if v == min(occurrence_dict.values())]
        # Return type is a List
        return min_value

    def is_str_a_palindrome(_inp_str):
        '''
        Method to check if a string is a palindrome
        Argument to this method: string
        '''
        reversed_string = _inp_str[::-1]
        return True if _inp_str == reversed_string else False

    def join_dicts_and_sort(*_dicts_iterables, _sort_key='key', _sort_reversal=False):
        '''
        Method to join multiple dictionaries to a single dictionary and sort the new dictionary based on keys or values in
        Ascending or Descending order
        Argument to this method: Multiple Dictionaries as arguments (separated by comma), sorting key and sorting type
        * takes care of the unpacking multiple dictionaries passed as arguments
        _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
        _sort_key='value' will sort the resulting dictionary by values in ascending order
        _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order
        '''
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Sort the updated dictionary based on keys in ascending order
        # usage of sorted method: sorted(iterable, key)
        # special note: key can be any user defined function as well
        # for sorting key, I am using the anonymous lambda function and item[0] refers to the dictionary keys
        if _sort_key == 'key':
            # Return type is a dictionary
            return dict(sorted(merged_dict.items(), key=lambda item:item[0], reverse=_sort_reversal))
        elif _sort_key == 'value':
            # Return type is a dictionary
            return dict(sorted(merged_dict.items(), key=lambda item:item[-1], reverse=_sort_reversal))

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
    
    def join_dicts_m2(*_dicts_iterables):
        '''
        Method to join multiple dictionaries to a single dictionary
        Argument to this method: Multiple Dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        chained_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            chained_dict.update(_)
        # Return type is a dictionary
        return chained_dict

    def join_dicts_m3(*_dicts_iterables):
        '''
        Method to join multiple dictionaries to a single dictionary
        Argument to this method: Multiple Dictionaries as arguments (separated by comma)
        * takes care of the unpacking multiple dictionaries passed as arguments
        '''
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Return type is a dictionary
        return merged_dict

    def join_lists(*_lists_iterables):
        '''
        Method to join multiple lists into one list
        Argument to this method: Multiple lists as arguments (separated by comma)
        * takes care of the unpacking multiple lists passed as arguments
        '''
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterables))
        # Return type is a list
        return chained_list

    def join_tuples(*_tuple_iterables):
        '''
        Method to join multiple tuple arguments into one tuple
        Arguments to this method: Multiple tuples as arguments (separated by comma)
        * takes care of the unpacking multiple tuples passed as arguments
        '''
        # itertools.chain : joins multiple tuples in to one
        joined_tuple = _tuple_iterables.__class__(itertools.chain(*_tuple_iterables))
        # Return type is a tuple
        return joined_tuple

    def lists_to_dict(key_list, val_list):
        '''
        Method to create a dictionary based on two lists
        Argument to this method: Two lists
        Elements of 1st list are treated as 'Keys' and 2nd list as 'Values'        
        '''
        # Return type is a dictionary
        return dict(zip(key_list, val_list))

    def merge_lists(*_lists_iterables):
        '''
        Method to join multiple lists into one list and keep only non-repeating values
        Argument to this method: Multiple lists as arguments (separated by comma)
        * takes care of the unpacking multiple lists passed as arguments
        '''
        # itertools.chain : joins the multiple lists into one
        # set removes the duplicate entries from the list
        # list converts the unique set to a list
        merged_list = list(set(list(itertools.chain(*_lists_iterables))))
        # Return type is a list
        return merged_list

    def merge_tuples(*_tuple_iterables):
        '''
        Method to join multiple tuples arguments into one tuple and remove duplicate elements from result tuple
        Arguments to this method: Multiple tuples as arguments (separated by comma)
        * takes care of the unpacking multiple tuples passed as arguments
        '''
        # itertools.chain : joins multiple tuples in to one
        # set : removes the duplicate elements from the result
        joined_tuple = tuple(set(itertools.chain(*_tuple_iterables)))
        # Return type is a tuple
        return joined_tuple

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

    def reverse_string(_inp_str):
        '''
        Method to reverse the string
        Argument to this method: string
        '''
        # Return type is a string
        return _inp_str[::-1]

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

    def top_5_elem_occurrences_in_str(_inp_str):
        '''
        Method to get top 5 alphabets based on their occurrences in string
        Argument to this method: string
        '''
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(5))

    def top_n_elem_occurrences_in_str(_inp_str, n):
        '''
        Method to get top n alphabets based on their occurrences in string
        Argument to this method: string, and n = Integer
        '''
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(n))