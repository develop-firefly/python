def df_sort_row_level_diff_cols(self, _src_col_name, _tgt_col_name, _delim, _sort_type,
                                _str_join_param):
    '''
    Method sorts the data in a column at row level (basically each cell of a column)
    Input:1 - _src_col_name: The column which has the unsorted data
    Input:2 - _tgt_col_name: The column where sorted data will be written
    Input:3 - _delim: The current delimiter of the dataset in the cell
    Input:4 - _sort_type: Can be 'asc' or 'desc'
    Input:5 - _str_join_param: User provided _delim to join the strings
    Output: DataFrame with sorted data in target column
    '''
    for item in range(0, self.my_df[_src_col_name].shape[0]):
        if _sort_type == 'asc':
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # LHS:- Following line accesses the particular cell
            # item is row index and _col_name is column index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_position, column_position]
            self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=False))
        elif _sort_type == 'desc':
            self.my_df.loc[item, _tgt_col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _src_col_name].split(_delim), reverse=True))
    return self.my_df