def drop_last_col(self):
    '''
    Method to Drop the last column of the dataframe
    Note: This method assumes that there's at least 1 column in the dataframe
    Input: - None
    Output: - 'dataframe is empty' if dataframe has no columns
    '''
    if len(self.my_df.columns.values) > 0:
        self.my_df.drop(self.my_df.columns[-1], axis=1, inplace=True)
    return 'dataframe is empty'