def drop_col_by_name(self, _col_name):
    '''
    Method to remove a column from the dataframe
    Note: This method is build using a try: except block to deal with spelling mistakes in column name
    Input: - Column name
    Output: - None
    '''
    try:
        self.my_df.drop(_col_name, axis=1, inplace=True)
        # print(f'Column Name "{_col_name}" removed successfully from the dataframe')
    except KeyError:
        print(f'Error:- Column Name "{_col_name}" is not present in the dataframe')