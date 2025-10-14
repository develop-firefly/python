def get_specific_row_col_val_based_on_row_range(self, _row_start, _row_end, _col_names_list):
    '''
    Method to get values from specific rows based on a row range for selected columns (inclusive of ending row)
    Input: - starting row index, ending row index and list with column names
    Only selected columns will be printed based on the column names provided
    Output: - DataFrame containing the rows in the specified range for the selected columns
'''
    # The columns name(s) provided should be in a list, other iterable methods will not work
    if isinstance(_col_names_list, list):
        # using list comprehension, get the index of the columns
        _col_idx_list = [self.get_col_idx_by_name(_) for _ in _col_names_list]
        # Ending row index must be greater than the starting row index
        if _row_end > _row_start:
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
            # If column indexes are not provided, then all columns will be selected by default
            # A list containing column indexes can also be used
            return self.my_df.iloc[_row_start:_row_end + 1, _col_idx_list]
    else:
        print('Column Names must be in a list')