def df_standardize_delim(self, _col_name, _delim):
    '''
    Method to Standardize delimiters in a specified DataFrame column.
    Parameters:
    Input:1 _col_name (str): The name of the column to standardize.
    Input:2 _delim (str): The delimiter to standardize to.
    Output: The modified column with standardized delimiters.
    '''
    to_replace = [", ", ",", "'", "; ", " ; ", " ", "\\", ";;", "-", "/", ",;"]
    for item in to_replace:
        # Assign the formatted value to the column
        self.my_df[_col_name] = self.my_df[_col_name].str.replace(item, _delim, regex=True)
    return self.my_df[_col_name]