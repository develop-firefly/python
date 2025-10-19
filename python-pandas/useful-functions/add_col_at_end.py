def add_col_at_end(self, _col_name):
    '''
    Method to add a new column at the end of the dataframe.
    Input: Column name of user choice.
    Output: None
    '''
    # The following statement checks if the user provided column name already exists in the dataframe or not
    # The new column will only be added if it does not exist already
    if _col_name not in self.my_df.columns:
        # shape returns a tuple of (row count, column count)
        return self.my_df.insert(self.my_df.shape[-1], _col_name, '', True)
    # Else the new column name will not be added to the dataframe
    else:
        print(f'Column :- "{_col_name}" is already present in the Dataframe, skipping addition...', end='\n')
