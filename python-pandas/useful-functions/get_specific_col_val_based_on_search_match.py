def get_specific_col_val_based_on_search_match(self, _search_col_name, _search_val, _see_val_col_name):
    '''
    Method to get values of  specific columns if search value matched in another column
    Input: - Column Name to the searched,  Value to be searched, Values to be seen
    Output: - List of values from the column to be seen where the search value matched
    '''
    # get the column indexes
    _search_col_idx = self.get_col_idx_by_name(_search_col_name)
    _see_val_col_idx = self.get_col_idx_by_name(_see_val_col_name)
    return [_val[_see_val_col_idx + 1] for _val in
            [_ for _ in self.my_df.itertuples() if _[_search_col_idx + 1] == _search_val]]
