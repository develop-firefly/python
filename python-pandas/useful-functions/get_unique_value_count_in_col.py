def get_unique_value_count_in_col(self, _col_name):
    '''
    Method to get count of unique items in a given column
    Input: - Column name
    Output: - Count of unique items in the column
    '''
    return self.my_df[_col_name].nunique()