import collections

def top_5_elem_occurrences_in_str(_inp_str):
    '''
    Method to get top 5 alphabets based on their occurrences in string
    Argument to this method: string
    '''
    # We use the 'most_common' method for Counter
    return dict(collections.Counter(_inp_str).most_common(5))