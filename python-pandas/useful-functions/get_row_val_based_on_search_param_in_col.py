def get_row_val_based_on_search_param_in_col(self, _col_name, _search_val):
    '''
    Method to get row values based on a search param in a given column name
    Input: - Column name to be searched and search value
    Output: - List of rows where the search value matched in the given column
    '''
    _col_idx = self.get_col_idx_by_name(_col_name)
    # Return the entire row, if searched value was found in the given column
    return [_ for _ in self.my_df.itertuples() if _[_col_idx + 1] == _search_val]