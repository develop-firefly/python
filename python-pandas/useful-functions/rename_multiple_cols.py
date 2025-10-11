def rename_multiple_cols(self, _old_col_name_iterable, _new_col_name_iterable):
    '''
    Method to rename multiple columns at once
    Input Arguments: - Two iterables, first with the old column names
    And second with the new column names
    '''
    # The length of both the iterables must be same
    # Same number of column names in the list for replacement
    if len(_old_col_name_iterable) == len(_new_col_name_iterable):
        # Create a dictionary using the two lists
        _my_map = dict(zip(_old_col_name_iterable, _new_col_name_iterable))
        # Iterate over the key-value pair of the dictionary
        for _ocv, _ncv in _my_map.items():
            # Assign the renamed columns to original dataframe
            # so that changes are reflected in spreadsheet
            self.my_df = self.my_df.rename(columns={str(_ocv): str(_ncv)})