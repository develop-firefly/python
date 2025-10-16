def get_col_unique_values_by_idx(self, _col_idx):
    '''
    Method to get the unique values from a given column index position
    Input: - Column Index
    Output: - Numpy array of unique values
    '''
    # Return type is dependent on column values
    return self.my_df[self.my_df_col_idx_name[_col_idx]].unique()
