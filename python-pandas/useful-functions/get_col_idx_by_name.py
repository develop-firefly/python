def get_col_idx_by_name(self, _col_name):
    '''
    Method to get the column index based on column name
    Input: - Column name
    Output: - Column index (integer)
    '''
    # return type is integer
    # get_loc will get the index of the column
    return self.my_df.columns.get_loc(_col_name)