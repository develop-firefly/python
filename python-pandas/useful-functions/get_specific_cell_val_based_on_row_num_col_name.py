def get_specific_cell_val_based_on_row_num_col_name(self, _row_idx, _col_name):
    '''
    Method to get a cell value based on row index and column name
    Input: - Row index and Column name
    NOTE: - Only a single cell value will be returned, since the intersection is a row and column index
    Output: - Cell value at the intersection of the specified row and column
    '''
    # loc allows accessing columns by name
    # iloc allows accessing columns by their index
    # syntax for loc[row_label, column_label]
    return self.my_df.loc[_row_idx, _col_name]