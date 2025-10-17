def df_sort_row_level_same_col(self, _col_name, _delim, _sort_type, _str_join_param):
    '''
    Method to sort data in a column at row level (basically each cell of a column)
    Input:1 - Column Name:- Where Data Needs to be sorted
    Input:2 - _delim:- The current delimiter of the dataset in the cell
    Input:3 - _sort_type:- Can be 'asc' or 'desc
    Input:4 - _str_join_param:- User provided _delim to join the strings
    Important Note:- For this method to provide results, the column name in question must have data in it
    Output: - DataFrame with sorted data at row level in the specified column
    '''
    # The for loop will run for the number of rows in the dataframe
    for item in range(0, self.my_df.shape[0]):
        if _sort_type == 'asc':
            # loc allows accessing columns by name
            # iloc allows accessing columns by their index
            # LHS:- Following line accesses the particular cell
            # item is row index and _col_name is column index
            # syntax for loc[row_label, column_label]
            # syntax for iloc[row_position, column_position]
            self.my_df.loc[item, _col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _col_name].split(_delim), reverse=False))
        elif _sort_type == 'desc':
            self.my_df.loc[item, _col_name] = _str_join_param.join(
                sorted(self.my_df.loc[item, _col_name].split(_delim), reverse=True))
    return self.my_df