def get_specific_row_val_based_on_row_range(self, _row_start, _row_end):
    '''
    Method to get values from specific rows based on a row range (inclusive of ending row)
    Input: - starting row index and ending row index
    NOTE: - All column values will be fetched by this method
    Output: - DataFrame containing the rows in the specified range
    '''
    # Ending row index must be greater than the starting row index
    if _row_end > _row_start:
        # loc allows accessing columns by name
        # iloc allows accessing columns by their index
        # syntax for loc[row_label, column_label]
        # syntax for iloc[row_idx_start:row_idx_end, col_idx_start:col_idx_end]
        # If column indexes are not provided, then all columns will be selected by default
        return self.my_df.iloc[_row_start:_row_end + 1]