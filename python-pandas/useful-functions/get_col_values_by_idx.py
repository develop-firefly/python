def get_col_values_by_idx(self, _col_idx):
    '''
    Method to Get the values from a given column index position
    Input: - Column index position
    Output: - Series containing the values in the specified column
    '''
    return self.my_df[self.my_df_col_idx_name[_col_idx]]