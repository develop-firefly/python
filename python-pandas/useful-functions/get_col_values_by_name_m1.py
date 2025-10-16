def get_col_values_by_name_m1(self, _col_name):
    '''
    Method to get the values from a given column
    Input: - Column name
    Output: - Series containing the values in the specified column
    '''
    # Return type is dependent on column values
    return self.my_df[_col_name]