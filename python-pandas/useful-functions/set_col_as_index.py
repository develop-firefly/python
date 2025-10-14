def set_col_as_index(self, _col_name):
    '''
    Method to set a column as the index column
    Input: - Column name which needs to be set as index
    Output: - DataFrame with the specified column set as index
    '''
    return self.my_df.set_index(_col_name)