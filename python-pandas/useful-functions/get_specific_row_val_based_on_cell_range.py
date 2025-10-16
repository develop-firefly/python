def get_specific_row_val_based_on_cell_range(self, _row_start, _row_end, _start_col_name, _end_col_name):
    '''
    Method to get values from specific rows based on a cell range (inclusive of ending row and column)
    Input: - starting row index, ending row index,
    Starting column name and Ending column name
    Output: - DataFrame containing the rows and columns in the specified range
    '''
    # Get the index based on the starting column name
    _start_col_idx = self.get_col_idx_by_name(_start_col_name)
    # Get the index based on the ending column name
    _end_col_idx = self.get_col_idx_by_name(_end_col_name)
    # Ending row index must be greater than the starting row index
    if _row_end > _row_start:
        # loc allows accessing columns by name
        # iloc allows accessing columns by their index
        # syntax for loc[row_label, column_label]
        # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
        return self.my_df.iloc[_row_start:_row_end + 1, _start_col_idx:_end_col_idx + 1]