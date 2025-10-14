def value_frequency_in_col_by_idx(self, _col_idx):
    '''
    Method to get frequency of occurrences per unique item in a given column
    Input: - Column index position
    Output: - Series with unique items as index and their frequency as values
    '''
    return self.my_df[self.my_df_col_idx_name[_col_idx]].value_counts()